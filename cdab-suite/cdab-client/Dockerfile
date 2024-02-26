FROM python:3.12-slim

# Impostazione della cartella di lavoro
WORKDIR /app

# Copia dei files necessari per utilizzare l'applicazione
COPY ./cdab-client.py ./requirements.txt /app/

# Installazione delle dipendenze dell'applicazione
RUN pip3 install -r requirements.txt --no-cache-dir

# Avvio dell'applicazione
CMD ["/bin/bash"]