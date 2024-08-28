from flask import request, jsonify
from app import app
from app.utils import get_db_connection

@app.route('/add_product', methods=['POST'])
def add_product():
    data = request.json
    nome = data['nome']
    codice_barre = data['codice_barre']
    prezzo = data['prezzo']

    conn = get_db_connection()
    cursor = conn.cursor()
    query = "INSERT INTO prodotti (nome, codice_barre, prezzo) VALUES (%s, %s, %s)"
    cursor.execute(query, (nome, codice_barre, prezzo))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "Prodotto aggiunto con successo!"})