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

## Creazione dei servizi

### Servizio `cdab-client`

Il primo servizio che andremo a creare e' `cdab-client`, poiche' senza questo servizio, i dati non possono essere estrapolati e passati agli altri servizi per essere processati.

Dopo aver creato una cartella per l'applicazione, passiamo alla creazione dell'ambiente virtuale, all'interno del quale, dopo averlo opportunamente attivato, andremo a installare le due librerie necessarie, ovvero _requests_ e _geopy_, utilizzando i comandi:

```console
pip install geopy
pip install requests
```

Una volta installate le librerie sopra riportate, possiamo passare all'esportazione dei requisiti per poterli copiare all'interno del container per la successiva installazione degli stessi, utilizzando il comando:

```
pip freeze > requirements.txt
```

Completato questo passaggio, possiamo definire il [Dockerfile](/cdab-client/Dockerfile), ovvero la base del container che eseguira' il servizio.

Ora, possiamo dare uno sguardo al codice presente nello script [cdab-client.py](./cdab-client/cdab-client.py)

### Servizio `cdab-scripts`

Il secondo servizio che andremo a creare e' `cdab-scripts`.

Dopo aver creato una cartella per l'applicazione, passiamo alla creazione dell'ambiente virtuale, all'interno del quale, dopo averlo opportunamente attivato, andremo a installare le due librerie necessarie, ovvero _mysql-connector-python_ e _python-dotenv_, utilizzando i comandi:

```console
pip install mysql-connector-python
pip install python-dotenv
```

Una volta installate le librerie sopra riportate, possiamo passare all'esportazione dei requisiti per poterli copiare all'interno del container per la successiva installazione degli stessi, utilizzando il comando:

```
pip freeze > requirements.txt
```

Completato questo passaggio, possiamo definire il [Dockerfile](/cdab-scripts/Dockerfile), ovvero la base del container che eseguira' il servizio.

E' doveroso dare uno sguardo al file [.env](/cdab-scripts/.env)

Ora, possiamo dare uno sguardo al codice presente nello script [cdab-load_data_to_mysql.py](./cdab-scripts/cdab-load_data_to_mysql.py)

### Servizio `cdab-db`

Il terzo e ultimo servizio che andremo a creare e' `cdab-db`.
Questo servizio non ha un Dockerfile dedicato, poiche' utilizzeremo direttamente l'immagine Docker ufficiale di MySQL.

## Creazione dell'infrastruttura

Una volta descritta l'infrastruttura della suite e delle sue componenti, possiamo procedere con la creazione (o build) della stessa, utilizzando il comando:

```console
docker compose up --detatch
```

Per stoppare e cancellare la suite, si puo' utilizzare il comando: 

```console
docker compose down --volumes
```

il quale, con il flag `--volumes`, provvede a eliminare i volumi non utilizzati dai containers.

## Utilizzo della suite

Ora che la suite e' configurata ed avviata, possiamo iniziare a utilizzarla.

Il primo comando da lanciare per far si' che i dati possano essere ottenuti dalle REST APIs ([Open-Meteo](https://open-meteo.com/en/docs/)) e':

```console
docker container exec cdab-client python cdab-client.py --lat 45.464664 --lon 9.188540 --variables "temperature_2m"
```

Questo comando generera' un file con estensione JSON, il quale potra' essere processato dallo script *cdab-load_data_to_mysql.py* nel container `cdab-scripts`.<br>
Per importare tale file nel DB MySQL, dobbiamo prima copiarlo localmente, utilizzando il comando

```console
docker cp cdab-client:/app/Milano_forecast_7_days.json .
```

Una volta copiato il file localmente, possiamo copiarlo nel container di destinazione, ovvero `cdab-scripts`, utilizzando il comando:

```console
docker cp Milano_forecast_7_days.json cdab-scripts:/app/
```

Una volta copiato il file nel container, possiamo iniziare il processo di importazione del file utilizzando il comando:

```console
docker container exec --interactive cdab-scripts python cdab-load_data_to_mysql.py
```

Per verificare che i dati siano stati correttamente importati, possiamo utilizzare la sessione TTY di MySQL, connettendoci al DB con il comando:

```console
mysql --host=localhost --database=cdab-db --user=superuser --password=some-random-password
```

ed eseguendo la query:

```sql
SELECT BIN_TO_UUID(`values`.id) as id, 
       `values`.timestamp,
       variables.name,
       `values`.value
FROM `cdab-db`.values 
RIGHT JOIN `cdab-db`.variables
ON variables.id = `values`.variable_id
WHERE variables.name = 'temperature_2m'
ORDER BY timestamp;
```

**Nota Bene:** il nome della tabella _values_ e' tra due backtick perche' values e' una parola chiave riservata di MySQL, che non potrebbe essere utilizzata come nome di una tabella.
