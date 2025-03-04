# Importazione del modulo Python Flask
from flask import Flask


# Il costruttore di Flask utilizza il nome del modulo corrente
app = Flask(__name__)


# La funzione route() è un decorator,
# Lega un URL a una funzione associata
@app.route('/')
def hello_world():
return 'Hello World'


# Se il file viene eseguito direttamente
# Eseguire l'applicazione Flask
if __name__ == '__main__':
app.run(debug=True, host='0.0.0.0')