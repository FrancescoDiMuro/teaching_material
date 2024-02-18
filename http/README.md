# HTTP
## Indice:
- [Definizione di HTTP](#definizione-di-http)
- [Metodi HTTP](#metodi-http)
- [Status Codes](#status-codes)
- [Struttura di una richiesta](#struttura-di-una-richiesta)
- [Struttura di una risposta](#struttura-di-una-risposta)
- [Formato di una richiesta e di una risposta](#formato-di-una-richiesta-e-di-una-risposta)

## Definizione di HTTP
HTTP e' l'acronimo di **H**yper**T**ext **T**ransfer **P**rotocol, ed e' il protocollo piu' utilizzato nel web per la gestione delle risorse con una struttura server-client.<br>
La richiesta di accesso alle risorse e' effettuata da uno o piu' client, il quale invia una richiesta al server che, una volta elaborata, ritorna una risposta con la risorsa richiesta.

[Torna all'indice ↑](#indice)

## Metodi HTTP
L'accesso alle risorse del server e' effettuato attraverso una richiesta di uno o piu' client, il quale, con l'utilizzo di un metodo HTTP, specifica in maniera precisa il tipo di azione che si vuole compiere con la risorsa.<br>
I metodi HTTP possono essere suddivisi in quattro categorie differenti, le quali assumono l'acronimo di *CRUD*, ovvero **C**reate, **R**etrieve, **U**pdate e **D**elete.
I metodi, suddivisi per categoria, sono:
- Create -> POST
- Retrieve -> GET
- Update -> PUT, PATCH
- Delete -> DELETE

Immaginiamo di voler ottenere i post scritti da un determinato utente (U) su un blog;
in pseudocodice, l'istruzione piu' adatta per una richiesta del genere sarebbe:

*"ottieni i post dell'utente U"* , che tradotto in inglese diventa *"retrieve U user's posts"*, il che si avvicina alla forma della richiesta che dovremmo fare per ottenere il risultato desiderato.

Traducendo lo pseudocodice con i metodi HTTP, la richiesta diventa:

`GET /users/{user_id}/posts` 

dove {user_id} e' un codice identificativo dell'utente U del quale si vogliono ottenere i posts.

[Torna all'indice ↑](#indice)

## Status Codes
Come abbiamo visto in precedenza, il processo di richiesta di una risorsa inizia con il tipo di operazione che si vuole fare verso la risorsa stessa, attraverso un metodo HTTP.<br>
Ma come fa un client a sapere che la richiesta e' stata presa in carico, e che, eventualmente, questa sia andata a buon fine, ritornando una risposta?<br>
Ed e' qui che subentra lo status code, ovvero un codice numerico ritornato dal server a seguito di una richiesta dal client, il quale identifica lo stato della richiesta stessa.

Anche per gli status codes ci sono differenti tipologie, le quali possono essere suddivise in:
- **1xx:** messaggi informativi
- **2xx:** messaggi di successo
- **3xx:** messaggi di reindirizzamento
- **4xx:** messaggi di errore da parte del client
- **5xx:** messaggi di errore da parte del server

Riprendendo l'esempio di prima, effettuando la richiesta specificata, il server, in caso di successo, ritornera' lo status code 200 (OK), il quale indica che la richiesta e' andata a buon fine.

Nel caso in cui una risorsa non fosse disponibile, il server ritornera' una risposta con lo status code uguale a 404 (NOT FOUND).

[Torna all'indice ↑](#indice)

## Struttura di una richiesta

Per far si' che il server possa processare la richiesta di un client in maniera corretta, questa deve avere una struttura ben precisa.<br>
Sebbene ogni richiesta abbia dei parametri specifici, tutte le richieste hanno una forma comune, la quale comprende:
- gli headers della richiesta
- il body della richiesta (opzionale)
- uno o piu' path parameters (opzionali)
- uno o piu' query parameters (opzionali)

All'interno dell'header, si possono trovare i parametri di intestazione della richiesta, i quali specificano il tipo di client si sta utilizzando, cosi' come il formato della richiesta, e tante altre impostazioni.

All'interno del body (o payload) della richiesta, si possono trovare i dati che devono essere inseriti o modificati riguardo la risorsa con la quale si sta interagendo, come per una richiesta POST o PUT/PATCH.

[Torna all'indice ↑](#indice)

## Struttura di una risposta

Una volta che la richiesta da parte del client e' stata presa in carico dal server, e la sua elaborazione e' stata portata a termine, questo provvede a dare una risposta che, come per la richiesta, ha una struttura ben precisa.<br>
Cosi' come per il client, ogni risposta cambia nella struttura del contenuto, mantenendo sempre delle parti in comune, tra le quali:
- gli headers della risposta
- lo stato della risposta (status code)
- il body della risposta

[Torna all'indice ↑](#indice)

## Formato di una richiesta e di una risposta
Ora che abbiamo visto la stuttura di una richiesta e di una risposta HTTP, andiamo a vedere i formati che queste possono assumere, affinche' il client e il server possano interpretare e utilizzare il loro contenuto in maniera corretta.

[Torna all'indice ↑](#indice)

### JSON
Il formato piu' utilizzato per effettuare una richiesta e' il JSON, acronimo di **J**ava**S**script **Object** **N**otation.<br>
Grazie a questo formato, ogni informazione e' rappresentata da un oggetto il quale, attraverso una struttura chiave-valore, permette al client/server di interpretare i dati in maniera corretta.
Per via della sua semplice struttura, questo tipo di formato e' altamente human-readable, dando modo di essere letto e interpretato in maniera intuitiva anche da un essere umano.


#### Esempio:
```json
{
    "user_id": 1,
    "name": "Mario",
    "surname": "Rossi",
    "email": "mario.rossi@gmail.com",
    "phones": [
        1, 2, 3, 4
    ]
}
```

[Torna all'indice ↑](#indice)

### XML
Un altro tipo di formato che viene utilizzato per lo scambio di informazioni utilizzando il protocollo HTTP e' XML, acronimo di E**X**tensbile **M**arkup **L**anguage.<br>
Questo tipo di formato propone una struttura associativa utilizzando dei tags, ai quali vengono associate le varie informazioni.<br>
Per via della sua struttura verbosa, l'XML viene utilizzato molto meno rispetto al JSON, oltre al fatto che questo sia un markup language (e che quindi richiede un interprete per essere correttamente elaborato), e non un formato di dati come il JSON.

#### Esempio
```xml
<book>
    <title>Learning Amazon Web Services</title>
    <author>Mark Wilkins</author>
</book>
```

[Torna all'indice ↑](#indice)
