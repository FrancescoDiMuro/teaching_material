## Definizione della struttura dell'applicazione
Per prima cosa, e' necessario individuare quali sono i servizi che devono essere creati affinche' l'applicazione funzioni come vogliamo.

Sappiamo che, per far si' che la Test Suite funzioni correttamente, l'architettura del progetto deve predisporre un container per lanciare i vari test case e un database MySQL nel quale importare i dati attraverso gli script predisposti;<br>
conseguentemente, questa prevedera' un servizio per il client cadb, un servizio per lanciare gli scripts di importazione dati nel db, e un servizio per il db.

La struttura dell'applicazione sara' quindi composta da tre servizi:
1. cdab-client
2. cdab-scripts
3. cdab-db

Grazie a questa definizione, possiamo iniziare a comporre l'infrastruttura dell'applicazione.

## Composizione del file compose.yaml
Il punto di partenza per lo sviluppo di quest'applicazione e' il file [compose.yaml](compose.yaml), grazie al quale viene implementata la struttura del progetto precedentemente analizzata e descritta.<br>
Iniziamo quindi a dare forma all'applicazione con la suddivisione dei vari servizi.

### Servizio `cdab-client`

python -m pip install mysql-connector-python

python -m pip install python-dotenv

pip freeze > requirements.txt

docker compose up --detatch

docker cp .\main.py cdab-client:/app/main.py

docker container start cdab-client --attach

docker compose down --rmi local