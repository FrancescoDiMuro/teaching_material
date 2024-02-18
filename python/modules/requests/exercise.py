# Traccia dell'esercizio:
# dato il BASE_URL, si vuole ottenere la lista dei "todos" per uno specifico utente.
# Nota Bene: fare attenzione a dove passare il parametro dello user_id!

import requests


BASE_URL: str = 'https://jsonplaceholder.typicode.com/'
USERS_ENDPOINT: str = 'users'
TODOS_ENDPOINT: str = 'todos'
user_id: int = 1


# ---------- Ottenimento dei todos dell\'utente con id = user_id ----------
    
print(f'{'-' * 10} Ottenimento dei posts dell\'utente con id = user_id ({user_id}) {'-' * 10}')

# Composizione dell'URL della richiesta
request_url: str = f'{BASE_URL}/{USERS_ENDPOINT}/{user_id}/{TODOS_ENDPOINT}'

# Utilizzo del metodo HTTP "GET" per ottenere la risorsa richiesta,
# e salvataggio del risultato della richiesta nella variabile "response"
response: requests.Response = requests.get(url=request_url)

# Se la richiesta e' andata a buon fine (response status_code = 200 -> OK)
if response.status_code == 200:
    print(f'Stato della Risposta => {response.status_code}')

    # Ottenimento del body della risposta in formato JSON
    response_body: list[dict] = response.json()

    # Ottenimento dei todos per l'utente con id = user_id
    user_todos: list[bool] = [todo['completed'] for todo in response_body]

    # Visualizzazione di tutti i todos dell'utente
    for i, todo_status in enumerate(user_todos):
        print(f'Stato Todo #{i + 1}: {'Completo' if todo_status else 'Incompleto'}')
