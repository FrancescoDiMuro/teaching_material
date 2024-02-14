# HTTP & Python requests
## Indice:
- [Definizione di HTTP](#definizione-di-http)
- [Metodi HTTP](#metodi-http)
- [Status Codes](#status-codes)
- [Struttura di una richiesta](#struttura-di-una-richiesta)
- [Struttura di una risposta](#struttura-di-una-risposta)
- [Creazione e attivazione dell'ambiente virtuale]()
- [Esempio pratico]()

## Definizione di HTTP
HTTP e' l'acronimo di **H**yper**T**ext **T**ransfer **P**rotocol, ed e' il protocollo piu' utilizzato nel web per la gestione delle risorse con una struttura server-client.<br>
La richiesta di accesso alle risorse e' effettuato da uno o piu' client, il quale invia una richiesta al server che, una volta elaborata, ritorna una risposta con la risorsa richiesta.

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
Ma come fa un client ha sapere che la richiesta e' stata presa in carico, e che, eventualmente, questa sia andata a buon fine, ritornando una risposta?
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
