from flask import Flask, request
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def hello():
    return "benvenuto, prova le chiamate: \n " + \
        "- http://127.0.0.1:5000/utenti  per avere la lista degli utenti con i ruoli associati \n " + \
        "- http://127.0.0.1:5000/ruoli  per avere la lista dei ruoli \n " + \
        "- http://127.0.0.1:5000/add-ruolo?nome=admin  per inserire un nuovo ruolo \n " + \
        "- http://127.0.0.1:5000/add-utente?utente=marco&ruolo=admin  per inserire un nuovo utente con un ruolo associato \n " + \
        "- http://127.0.0.1:5000/add-ruolo-to-utente?utente=marco&ruolo=admin  per aggiungere un ruolo ad un utente"

# restituisce la lista degli utenti con i ruoli associati
@app.route('/utenti')
def get_utenti():
    conn = get_db_connection()
    data = []
    for utente in conn.execute('SELECT * FROM relazione'):
        data.append(list(utente))
    conn.commit()
    conn.close()
    return data

# restituisce la lista dei ruoli
@app.route('/ruoli')
def get_ruoli():
    conn = get_db_connection()
    data = []
    for ruolo in conn.execute('SELECT * FROM ruolo'):
        data.append(list(ruolo))
    conn.commit()
    conn.close()
    return data

# aggiunge un nuovo ruolo e restituisce la lista dei ruoli
@app.route('/add-ruolo')
def add_ruolo():
    conn = get_db_connection()
    conn.execute("INSERT INTO ruolo (nome) VALUES ('" + request.args.get('nome') + "')")
    data = []
    for ruolo in conn.execute('SELECT * FROM ruolo'):
        data.append(list(ruolo))
    conn.commit()
    conn.close()
    return data

# aggiunge un utente, gli associa un ruolo e restituisce la lista degli utenti
@app.route('/add-utente')
def add_utente():
    conn = get_db_connection()
    conn.execute("INSERT INTO utente (nome) VALUES ('" + request.args.get('utente') + "')")
    conn.execute("INSERT INTO relazione (utente, ruolo) VALUES ('" + request.args.get('utente') + "', '" + request.args.get('ruolo') + "')")
    data = []
    for utente in conn.execute('SELECT * FROM utente'):
        data.append(list(utente))
    conn.commit()
    conn.close()
    return data

# aggiunge ad un utente un ruolo e restituisce la lista degli utenti con i ruoli associati
@app.route('/add-ruolo-to-utente')
def add_ruolo_to_utente():
    conn = get_db_connection()
    conn.execute("INSERT INTO relazione (utente, ruolo) VALUES ('" + request.args.get('utente') + "', '" + request.args.get('ruolo') + "')")
    data = []
    for utente in conn.execute('SELECT * FROM relazione GROUP BY utente'):
        data.append(list(utente))
    conn.commit()
    conn.close()
    return data