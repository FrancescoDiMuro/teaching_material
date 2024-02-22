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

# Lista dei records da inserire nella tabella "users"
USERS: list[dict] = [
    {
        'id': 1,
        'name': 'Mario',
        'surname': 'Rossi',
        'email': 'mario.rossi@gmail.com'
    },
    {
        'id': 2,
        'name': 'Giuseppe',
        'surname': 'Verdi',
        'email': 'giuseppe.verdi@gmail.com'
    }
]

# Lista dei records da inserire nella tabella "posts"
POSTS: list[dict] = [
    {
        'id': 1,
        'title': 'Titolo del post #1',
        'body': 'Body del post #1',
        'userId': 1
    },
    {
        'id': 2,
        'title': 'Titolo del post #2',
        'body': 'Body del post #2',
        'userId': 1
    },
    {
        'id': 3,
        'title': 'Titolo del post #3',
        'body': 'Body del post #3',
        'userId': 1
    },
    {
        'id': 4,
        'title': 'Titolo del post #4',
        'body': 'Body del post #4',
        'userId': 2
    },
    {
        'id': 5,
        'title': 'Titolo del post #5',
        'body': 'Body del post #5',
        'userId': 2
    }
]

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

    # Inserimento dei vari records (se non esistenti)
    for user in USERS:
        print(f'Sto creando l\'utente "{user['name']}"')
        user_insert_statement: str = '''INSERT IGNORE INTO users(id, name, surname, email)
                                        VALUES(%(id)s, %(name)s, %(surname)s, %(email)s);'''
        cursor.execute(user_insert_statement, user)

    for post in POSTS:
        print(f'Sto creando il post "{post['id']}"')
        post_insert_statement: str = '''INSERT IGNORE INTO posts(id, title, body, userId)
                                        VALUES(%(id)s, %(title)s, %(body)s, %(userId)s);'''
        cursor.execute(post_insert_statement, post)

    # Commit delle modifiche sul db
    connection.commit()
    
    print(f'{'-' * 10} SELECT di tutti i posts {'-' * 10}')
    
    # Query di SELECT
    select_users_statement: str = 'SELECT * FROM posts;'

    cursor.execute(select_users_statement)
    query_result = cursor.fetchall()
    
    # Per ogni riga nel cursore
    for i, row in enumerate(query_result):
        print(f'Post #{i} => {row}')

    print(f'{'-' * 10} SELECT di tutti i posts dello user con id = 1 {'-' * 10}')

    # Query di SELECT con WHERE
    select_users_statement: str = 'SELECT * FROM posts WHERE userId = 1;'

    cursor.execute(select_users_statement)

    # Per ogni riga nel cursore
    for i, row in enumerate(cursor):
        print(f'Post #{i} => {row}')

# Chiusura del cursore e della connessione con il db
cursor.close()
connection.close()
