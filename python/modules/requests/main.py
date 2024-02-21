import requests


# Definizione del Base URL, ovvero dell'Uniform Resource Locator
# di base per i vari endpoint
BASE_URL: str = 'https://jsonplaceholder.typicode.com/'

# Risorsa che vogliamo ottenere
POSTS_ENDPOINT: str = 'posts'

# ---------- Ottenimento dei titoli di tutti i posts ----------

print(f'{'-' * 10} Ottenimento dei titoli di tutti i posts {'-' * 10}')

# Composizione dell'URL della richiesta
request_url: str = f'{BASE_URL}/{POSTS_ENDPOINT}'

# Utilizzo del metodo HTTP "GET" per ottenere la risorsa richiesta,
# e salvataggio del risultato della richiesta nella variabile "response"
response: requests.Response = requests.get(url=request_url)

# Se la richiesta e' andata a buon fine (response status_code = 200 -> OK)
if response.status_code == 200:
    print(f'Stato della Risposta => {response.status_code}')

    # Ottenimento del body della risposta in formato JSON
    response_body: list[dict] = response.json()

    # Ottenimento dei titoli dei post dal response body
    post_titles: list[str] = [post['title'] for post in response_body]

    # Visualizzazione di tutti i titoli dei posts
    for i, post_title in enumerate(post_titles):
        print(f'Titolo del Post #{i + 1}: {post_title}')


# ---------- Ottenimento dei posts dell\'utente con id = userId ----------

# Impostazione di un query parameter
query_parameters: dict = {'userId': 5}

print(f'{'-' * 10} Ottenimento dei posts dell\'utente con id = userId ({query_parameters['userId']}) {'-' * 10}')

# Composizione dell'URL della richiesta
request_url: str = f'{BASE_URL}/{POSTS_ENDPOINT}'

# Utilizzo del metodo HTTP "GET" per ottenere la risorsa richiesta,
# e salvataggio del risultato della richiesta nella variabile "response"
response: requests.Response = requests.get(url=request_url, 
                                           params=query_parameters)

# Se la richiesta e' andata a buon fine (response status_code = 200 -> OK)
if response.status_code == 200:
    print(f'Stato della Risposta => {response.status_code}')

    # Ottenimento del body della risposta in formato JSON
    user_posts: list[dict] = response.json()

    # Ottenimento del numero di posts
    number_of_posts: int = len(user_posts)

    # Controllo sul numero di posts
    if number_of_posts > 0:
        print(f'L\'utente con id = {query_parameters['userId']} ha scritto {number_of_posts} ' \
              f'post{'s' if number_of_posts > 1 else ''}.')

        # Ottenimento dei titoli dei post dal response body    
        post_titles: list[str] = [post['title'] for post in user_posts]

        # Visualizzazione di tutti i titoli dei posts
        for i, post_title in enumerate(post_titles):
            print(f'Titolo del Post #{i + 1}: {post_title}')

    else:
        print(f'L\'utente con id = {query_parameters['userId']} non ha scritto nessun post.')
