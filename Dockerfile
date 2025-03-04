#Usa un'immagine base di Python
FROM python:3.10

# Imposta la directory di lavoro nel container
WORKDIR /app


# Copia il file requirements.txt nella directory di lavoro
COPY requirements.txt .


# Installa le dipendenze
RUN pip install --no-cache-dir -r requirements.txt


# Copia il resto del codice dell'applicazione
COPY . .


# Espone la porta su cui l'applicazione gira
EXPOSE 5000


# Definisce il comando per avviare l'applicazione
CMD ["python3", "app.py"]