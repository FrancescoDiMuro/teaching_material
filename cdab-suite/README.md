## Definizione della struttura dell'applicazione
Per prima cosa, e' necessario individuare quali sono i servizi che devono essere creati affinche' l'applicazione funzioni come vogliamo.

Sappiamo che, per far si' che la Test Suite funzioni correttamente, l'architettura del progetto deve predisporre un container per lanciare i vari test case e un database MySQL nel quale importare i dati attraverso gli script predisposti;<br>
conseguentemente, questa prevedera' un servizio per il client cdab, un servizio per lanciare gli scripts di importazione dati nel db, e un servizio per il database stesso.

La struttura dell'applicazione sara' quindi composta da tre servizi:
1. cdab-client
2. cdab-scripts
3. cdab-db

Con questa definizione, possiamo iniziare a comporre l'infrastruttura dell'applicazione.

## Composizione del file compose.yaml
Il punto di partenza per lo sviluppo di quest'applicazione e' il file [compose.yaml](compose.yaml), nel quale viene descritta la struttura del progetto precedentemente analizzata e descritta e, con un comando specifico, questa viene creata nell'ambiente Docker.<br>
Iniziamo quindi a dare forma all'applicazione con la suddivisione dei vari servizi.

### Servizio `cdab-client`
Il servizio cdab-client e' responsabile dell'ottenimento dei dati dalle test suites configurate.
Questo servizio estrapola i dati attraverso delle REST APIs, utilizzando i vari risultati per una successiva elaborazione con l'utilizzo degli scripts del servizio `cdab-scripts`.

### Servizio `cdab-scripts`
Il servizio cdab-scripts e' responsabile dell'esecuzione di scripts per l'estrapolazione e l'elaborazione dei dati ottenuti tramite il servizio `cdab-client`.

### Servizio `cdab-db`
Il servizio cdab-db e' responsabile della persistenza dei dati, grazie all'utilizzo di un database gestito da MySQL.<br>
Questo servizio si occupa di mantenere i dati in memoria, servendosi di un volume mappato all'host per rendere i dati persistenti e disponibili al servizio `cdab-scripts`.

## Scenario

Prima di dare uno sguardo all'infrastruttura vera e propria della suite `cdab-service`, e' doveroso descrivere lo scenario dell'applicazione, in modo tale da comprenderne la struttura in maniera completa.

Si pensi di voler estrapolare dei dati meteorologici da un servizio REST APIs, salvarli su un DB, e utilizzare i records salvati per effettuare dei calcoli e persistere i risultati su DB o su file.

Grazie a questa premessa, possiamo quindi fare un confronto tra la nostra infrastruttura e quella descritta dallo scenario, andando a confermare quelli che sono i ruoli dei vari servizi.

https://api.open-meteo.com/v1/


python -m pip install mysql-connector-python

python -m pip install python-dotenv

pip freeze > requirements.txt

docker compose up --detatch

docker compose down --rmi local

docker container exec cdab-client python cdab-client.py --lat 45.464664 --lon 9.188540 --variables "temperature_2m"
docker cp cdab-client:/app/Milano_forecast_7_days.json .
docker cp Milano_forecast_7_days.json cdab-scripts:/app/
docker container exec --interactive cdab-scripts python cdab-load_data_to_mysql.py

mysql --host=localhost --database=cdab-db --user=superuser --password=some-random-password

SELECT BIN_TO_UUID(`values`.id) as id, 
       `values`.timestamp,
       variables.name,
       `values`.value
FROM `cdab-db`.values 
RIGHT JOIN `cdab-db`.variables
ON variables.id = `values`.variable_id
WHERE variables.name = 'temperature_2m'
ORDER BY timestamp;

docker compose down --volumes
