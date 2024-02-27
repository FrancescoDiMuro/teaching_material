import json
import mysql.connector
import os
import logging
from dotenv import dotenv_values
from typing import OrderedDict
from uuid import uuid4


# Impostazione del logger di default
logging.basicConfig(level='DEBUG', format='%(name)s - %(asctime)s - %(message)s')

# Ottenimento delle variabili dal file .env in un dizionario
ENVIRONMENT_VARIABLES: OrderedDict = dotenv_values(dotenv_path='.env')

# Istruzione di CREATE per la tabella "variables"
variables_table_create_statement: str = '''CREATE TABLE IF NOT EXISTS `variables`
                                (
                                    id BINARY(16) NOT NULL,
                                    name VARCHAR(64) NOT NULL UNIQUE,
                                    PRIMARY KEY(id)
                                );'''

# Istruzione di CREATE per la tabella "values"                                
values_table_create_statement: str = '''CREATE TABLE IF NOT EXISTS `values`
                                (
                                    id BINARY(16) NOT NULL,
                                    timestamp DATETIME UNIQUE NOT NULL,
                                    variable_id BINARY(16) NOT NULL,
                                    value FLOAT(5),
                                    PRIMARY KEY(id),
                                    FOREIGN KEY(variable_id) REFERENCES variables(id)
                                );'''

# Connessione con il db MySQL
connection = mysql.connector.connect(user=ENVIRONMENT_VARIABLES['MYSQL_USER'], 
                                     password=ENVIRONMENT_VARIABLES['MYSQL_PASSWORD'],
                                     host=ENVIRONMENT_VARIABLES['MYSQL_HOSTNAME'],
                                     database=ENVIRONMENT_VARIABLES['MYSQL_DATABASE'], 
                                     port=ENVIRONMENT_VARIABLES['MYSQL_PORT'])

# Ottenimento dello stato di connessione con il db
is_connected: bool = connection.is_connected()
if is_connected:
    logging.debug(f'MySQL Connection Status => {'OK' if is_connected else 'ERR'}')

    # Ottenimento del cursore per interagire con il db
    cursor = connection.cursor(dictionary=True)

    # Creazione delle tabelle (se non esistenti)
    cursor.execute(variables_table_create_statement)
    cursor.execute(values_table_create_statement)

    # Ottenimento della lista dei files JSON da processare
    json_files_list: list[str] = [item for item in os.listdir('.') 
                                if os.path.isfile(item) and
                                item.endswith('.json')]

    logging.debug(f'Scanning for JSON files => Files found = {len(json_files_list)}')

    # Se e' stato trovato almeno un file da processare
    if len(json_files_list) > 0:
        logging.debug(f'{'-' * 10} Start processing JSON files {'-' * 10}')

    # Per ogni file nella file dei files
    for file in json_files_list:

        logging.debug(f'Processing file => "{file}"')

        # Apertura del file in modalita' "lettura"
        with open(file, 'r') as f:

            # Ottenimento del contenuto del file in formato JSON (dict)
            file_content_json = json.load(f)
            
        # Ottenimento (e cancellazione) dei timestamps dei valori delle variabili
        timestamps: list = file_content_json['hourly'].pop('time')

        # Ottenimento dei valori delle variabili (dict => {variable_name: [values]})
        data: dict = file_content_json['hourly']

        # Ottenimento della lista delle variabili da inserire nella tabella "variables"
        variables: list = [(uuid4().hex, key) for key in data.keys()]

        # Composizione della query di INSERT nella tabella "variables"
        variables_insert_statement: str = '''INSERT IGNORE INTO variables(id, name) 
                                            VALUES(UUID_TO_BIN(%s),
                                                %s
                                            );'''
        
        # Inserimento dei records nella tabella "variables"
        cursor.executemany(variables_insert_statement, variables)

        # Commit delle transazioni sul db
        connection.commit()

        # Query per selezionare le variabili dalla tabella "variables"
        variables_select_statement: str = 'SELECT BIN_TO_UUID(id) as id, name FROM variables;'

        # Esecuzione della query e ottenimento del risultato dello stesso
        cursor.execute(variables_select_statement)
        variable_ids: list = cursor.fetchall()

        # Per ogni variabile
        for variable in variable_ids:
            
            # Ottenimento dell'id e del nome della stessa
            variable_id, variable_name = variable.values()
            
            # Sostituzione della chiave nel dizionario (nome variabile) con l'id della variabile ,
            # mantenendo i valori
            data[variable_id] = data.pop(variable_name)

        # Definizione di una lista per il metodo "executemany" di INSERT
        insert_data: list = []

        # Per ogni variabile
        for variable_id, values in data.items():
            
            # Zip delle due liste (timestamps e values)
            data[variable_id] = list(zip(timestamps, values))

            # Per ogni dato della variabile (data[variable_id])
            for timestamp, value in data[variable_id]:

                # Aggiunta della riga da inserire nella tabella "values"
                insert_data.append((uuid4().hex, timestamp, variable_id, value))

        # Query di INSERT
        insert_statement: str = '''INSERT IGNORE INTO `values` (id, timestamp, variable_id, value) 
                                   VALUES(UUID_TO_BIN(%s), %s, UUID_TO_BIN(%s), %s);
                                   '''
        # Esecuzione della query di INSERT
        cursor.executemany(insert_statement, insert_data)
        
        # Se sono state inserite delle righe con l'ultima istruzione
        if cursor.rowcount > 0:
            logging.debug(f'"{file}" - Data loaded into DB (rowcount => {cursor.rowcount})')
            logging.debug(f'"{file}" - Deleting file "{file}"')
            
            # Eliminazione del file JSON (perche' e' stato processato)
            os.remove(file)
        else:
            logging.debug(f'"{file}" - Ignore data lodaing into DB (rowcount => {cursor.rowcount})')

    # Commit delle modifiche sul db
    connection.commit()
    
# Chiusura del cursore e della connessione con il db
cursor.close()
connection.close()
