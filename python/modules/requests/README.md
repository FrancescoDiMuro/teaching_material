# Python "requests" Module
## Indice:
- [Definizione](#definizione)
- [Creazione dell'ambiente virtuale](#creazione-dellambiente-virtuale)
- [Installazione del modulo](#installazione-del-modulo)
- [Utilizzo del modulo](#utilizzo-del-modulo)
- [Esercizio pratico](#esercizio-pratico)

## Definizione
Il modulo "requests" e' un modulo utilizzato per effettuare richieste con il protocollo HTTP attraverso il linguaggio Python.<br>
Tale modulo viene impiegato in differenti tipi di applicazioni, le quali spesso ottengono i dati attraverso delle APIs.

## Creazione dell'ambiente virtuale
Prima di iniziare a sviluppare, e' buona norma creare un ambiente virtuale in Python, grazie al quale, tutte le dipendenze necessarie per il funzionamento dell'applicazione che andremo a scrivere, saranno contenute in un ambiente sicuro e isolato dalle dipendenze globali (dove e' installato Python).

Per prima cosa, bisogna lanciare il comando per scaricare e installare il modulo _virtualenv_:
```console
[Cartella_di_installazione_di_Python]\python.exe -m pip install virtualenv
```

Dopo aver lanciato questo comando, il modulo _virtualenv_ verra' installato, e possiamo procedere con la creazione dell'ambiente virtuale.

Procediamo con creare una cartella all'interno della quale andremo a sviluppare lo script.<br>
Una volta creata la cartella, utilizzando il terminale di VSCode o un altro terminale, navigare all'interno della cartella e digitare il comando:

```console
[Cartella_di_installazione_di_Python]\python.exe -m virtualenv .\venv
```

Una volta completata l'esecuzione di questo comando, l'ambiente virtuale (d'ora in poi **venv**) sara' stato creato, dandoci modo di proseguire con l'attivazione dello stesso.<br>
Con questo passaggio, indichiamo all'editor del codice di utilizzare tutti gli scripts e le dipendenze all'interno del venv.
Per procedere con l'attivazione del _venv_, lanciamo il comando:

```console
[Cartella_del_venv]\Scripts\activate
```

**Nota Bene:** una volta attivato il venv, tutti gli scripts presenti all'interno di esso saranno eseguibili senza dover specificare il percorso in cui si trovano, ovvero:

```console
[Cartella_del_venv]\Scripts\python.exe -m pip install some-module
```

diventa

```console
python.exe -m pip install some-module
```

Completata l'esecuzione del comando sopra riportato, il venv sara' attivo e possiamo procedere con l'implementazione del codice in un ambiente isolato.

[Torna all'indice ↑](#indice)

## Installazione del modulo

Procediamo con l'installazione del modulo _requests_.

All'interno del terminale di VSCode (o di quello utilizzato), lanciare il comando:

```console
python.exe -m pip install requests
```

Una volta completata l'esecuzione del comando, il modulo requests e' installato correttamente, e possiamo procedere con il suo utilizzo.

[Torna all'indice ↑](#indice)

## Utilizzo del modulo

Per prima cosa, creiamo uno script con il quale interagiremo.<br>
Una volta creato lo script, possiamo iniziare a scrivere il codice per interagire con il modulo requests.<br>
Il codice che andremo a eseguire e' presente nel file [`main.py`](main.py) del repository corrente.

## Esercizio pratico

Ora che abbiamo visto come interagire con la libreria requests di Python, svolgi l'esercizio che puoi trovare nel file [`exercise.py`](exercise.py) del repository corrente.