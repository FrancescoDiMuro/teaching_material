import mysql.connector
from dotenv import dotenv_values
from typing import OrderedDict


# Ottenimento delle variabili dal file .env in un dizionario
ENVIRONMENT_VARIABLES: OrderedDict = dotenv_values(dotenv_path='.env')

# Istruzione di CREATE per la tabella "users"
users_table_create_statement: str = '''CREATE TABLE IF NOT EXISTS users
                                (
                                    id int NOT NULL,
                                    name varchar(255) NOT NULL,
                                    surname varchar(255) NOT NULL,
                                    email varchar(255) NOT NULL,
                                    PRIMARY KEY(id)
                                );'''

# Istruzione di CREATE per la tabella "posts"                                
posts_table_create_statement: str = '''CREATE TABLE IF NOT EXISTS posts
                                (
                                    id int NOT NULL,
                                    title varchar(255) NOT NULL,
                                    body varchar(255) NOT NULL,
                                    userId int NOT NULL,
                                    PRIMARY KEY(id),
                                    FOREIGN KEY(userId) REFERENCES users(id)
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
    print(f'MYSQL Connection Status => {'OK' if is_connected else 'ERR'}')

    # Ottenimento del cursore per interagire con il db
    cursor = connection.cursor(dictionary=True)

    # Creazione delle tabelle (se non esistenti)
    cursor.execute(users_table_create_statement)
    cursor.execute(posts_table_create_statement)

    # Commit delle modifiche sul db
    connection.commit()
    
# Chiusura del cursore e della connessione con il db
cursor.close()
connection.close()