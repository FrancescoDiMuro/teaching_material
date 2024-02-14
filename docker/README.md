# Docker
## Indice:
- [Definizione di Docker](#definizione-di-docker)
- [Installazione di Docker Desktop](#installazione-di-docker-desktop)
- [Images, Containers e Volumes](#images-containers-e-volumes)
- [Networks](#networks)
- [Creazione di un Docker container](#creazione-di-un-docker-container)
- [Docker Compose](#docker-compose)

## Definizione di Docker
Docker e' una piattaforma aperta per lo sviluppo, la distribuzione e l'esecuzione di applicazioni.<br>
Docker consente di separare le applicazioni dall'infrastruttura (host) in modo da poter distribuire rapidamente il software.<br>
Con Docker puoi gestire la tua infrastruttura nello stesso modo in cui gestisci le tue applicazioni.<br>
Sfruttando le metodologie di Docker per la spedizione, il test e la distribuzione del codice, puoi ridurre significativamente il ritardo tra la scrittura del codice e la sua esecuzione in produzione.

[Torna all'indice ↑](#indice)

## Installazione di Docker Desktop
Per poter installare Docker Desktop, e' necessario il file di setup, scaricabile da [qui](https://desktop.docker.com/win/main/amd64/Docker%20Desktop%20Installer.exe?utm_source=docker&utm_medium=webreferral&utm_campaign=dd-smartbutton&utm_location=module).

[Torna all'indice ↑](#indice)

## Images, Containers e Volumes
Una Docker *image* e' una tipologia di file utilizzato per eseguire codice in un contenitore Docker.<br>
Le immagini Docker fungono da set di istruzioni per creare un contenitore Docker, come un modello, cosi' come da punto di partenza quando si utilizza Docker.<br>
Un'immagine e' paragonabile a uno snapshot negli ambienti di macchine virtuali (VM).

Un Docker *container* e' un ambiente isolato per il tuo codice.<br>
Cio' significa che un contenitore non ha conoscenza del tuo sistema operativo o dei tuoi file, poiche' questo funziona nell'ambiente fornito da Docker Desktop<br>
I containers hanno tutto cio' di cui il tuo codice ha bisogno per essere eseguito, fino a un sistema operativo di base.<br>
Puoi utilizzare Docker Desktop per gestire ed esplorare i tuoi containers.

Un Docker *volume* e' un file system indipendente, interamente gestito da Docker ed esiste come un normale file o directory sull'host, dove i dati vengono salvati in maniera persistente.

[Torna all'indice ↑](#indice)

## Networks
Una Docker *network* e' una rete di contenitori che si riferisce alla capacità degli stessi di connettersi e comunicare tra di loro o con carichi di lavoro non Docker.

[Torna all'indice ↑](#indice)

### Nota Bene:
D'ora in poi, quando leggerai image, container, volume o network, sai che questi termini fanno riferimento all'ambiente Docker, finche' non viene diversamente specificato.

## Creazione di un Docker container
Ora che hai appreso le nozioni relative a cos'e' Docker e a tutte le sue componenti principali, puoi iniziare con la creazione del tuo primo Docker container.

Per poter creare un container, e' necessaria una image, che puoi creare in autonomia con un [Dockerfile](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/#:~:text=What%20is%20a%20Dockerfile%3F,can%20find%20at%20Dockerfile%20reference.) e una image dal [Docker Hub](https://hub.docker.com/).

In questo tutorial, creerai un container utilizzando il Dockerfile.

### Creazione del Dockerfile

Per prima cosa, e' necessario definire la struttura dell'immagine dalla quale il container si basera', e per soddisfare tale requisito, si puo' utilizzare il Dockerfile.

La prima istruzione che viene scritta nel Dockerfile fa riferimento al tipo di [sintassi](https://docs.docker.com/engine/reference/builder/#syntax) utilizzata nello stesso:

`syntax=docker/dockerfile:1`

dove *docker/* e' il nome del repository dal quale viene scaricato il file, e *dockerfile* e il nome del Dockerfile aggiornato all'ultima versione stabile dello stesso (*:1*) che viene comparato con il BuildKit.

Una volta specificata questa istruzione, si prosegue con l'istruzione `FROM`, la quale specifica da quale immagine basarsi per creare una nuova immagine.

In questo caso, l'immagine e' `python:3.12-slim`.

```docker
FROM python:3.12-slim
```

Ora che e' stata specificata l'immagine template, si prosegue con l'impostazione di alcuni parametri, tra i quali la direttori di lavoro, che conterra' l'applicazione che si intende eseguire, utilizzando l'istruzione `WORKDIR`:
```docker
WORKDIR /app
```

Una volta impostata la directory di lavoro dell'applicazione, si prosegue con la copia dell'applicazione stessa, che in questo caso e' `main.py`, utilizzando l'istruzione `COPY`:

```docker
COPY main.py /app
```

Ora che l'applicazione e' presente nell'immagine, si prosegue con l'ultima istruzione, ovvero quella che avvia l'applicazione quando il container viene avviato, ovvero l'istruzione `CMD`:

```docker
CMD ["python", "main.py"]
```

Bene!<br>
Il Dockerfile e' completo, e si puo' passare alla fase di build, ovvero la fase in cui l'immagine template viene costruita, facendo in modo tale che possa essere utilizzata per creare un container.

Per poter effettuare quanto descritto, e' necessario utilizzare i comandi di Docker attraverso la CLI (Command Line Interface), grazie ai quali verra' "buildata" l'immagine e, conseguentemente e con gli opportuni comandi, il container.

Il primo comando da utilizzare e' il seguente:
```console
docker image build --tag sample-image:latest .
```
Una volta buildata l'immagine, si puo' procedere con la creazione del container, specificando l'immagine template sulla quale questo si basera':

```console
docker container create --interactive --name sample-container sample-image:latest
```

Ora che il container e' stato creato, e' possibile avviarlo con il comando:

```console
docker container start sample-container
```

Il container, una volta avviato, eseguira' il comando specificato dall'istruzione `CMD` presente nel Dockerfile, e, una volta completata l'elaborazione dell'istruzione, il container verra' automaticamente arrestato.

Ci sono diversi parametri che possono essere specificati durante l'esecuzione dei vari comandi per gestire le immagini e i containers, tra i quali:
- <b>--tag</b>, per specificare il nome dell'image che si sta buildando;
- <b>--interactive</b>, per specificare che il container accettera' input dallo STDIN (da parte dell'utente);
- <b>--attach</b>, per specificare che il container reindirizzera' l'output verso lo STDOUT (da parte dell'applicazione);
- e molti altri!

Per una lista completa di parametri utilizzabili dai vari comandi, basta digitare il comando:
```console
docker [component] [--help]
```

e per un comando specifico:

```console
docker [component] [command] [--help]
```

## Docker Compose
Docker Compose è uno strumento per definire ed eseguire applicazioni multi-contenitore.<br>
Compose semplifica il controllo dell'intero stack di applicazioni, facilitando la gestione di servizi, reti e volumi in un unico file di configurazione YAML comprensibile, grazie al quale, con un solo comando, vengono creati e avviati tutti i servizi dal file di configurazione.

Le specifiche del file `compose.yaml` possono essere visualizzate [qui](https://docs.docker.com/compose/compose-file/).

### Struttura di un file compose.yaml
Come indicato nel paragrafo precedente, il file *compose.yaml* ha una struttura ben precisa, la quale dev'essere rispettata affinche', quando viene lanciato il comando per creare l'infrastruttura dell'app in Docker, questa venga riconosciuta e costruita in maniera corretta.

Vediamo un esempio di file compose.yaml:
```yaml
name: sample-app
services:
  app:
    build: .
    image: sample-image:latest
    container_name: sample-container
```

Andando ad analizzare i vari componenti del file, si puo' evidenziare una struttura con elementi top-level ed elementi annidati.

Tra gli elementi top-level possiamo trovare:
- `name`, il quale identifica il nome dell'applicazione nel suo insieme di containers;
- `services`, il quale identifica i vari containers.

Tra gli elementi annidati o "nested", possiamo trovare:
- `build` del container `app`, il quale identifica che l'immagine sulla quale si basa il container dev'essere buildata utilizzando il Dockerfile nella directory corrente;
- image del container `app`, il quale identifica che l'immagine sulla quale si basa il container e' quella specificata;
- `container_name`, il quale identifica il nome del container.

Una volta specificata la struttura dell'applicazione da containerizzazre nel file compose.yaml, si puo' procedere con la fase di building eseguendo il comando:

```console
docker compose up
```

il quale creera' e avviera' tutti i vari componenti specificati nel suddetto file di configurazione.

Se si intende arrestare ed eliminare l'app e le varie componenti, bastera' eseguire il comando:

```console
docker compose down
```

[Torna all'indice ↑](#indice)