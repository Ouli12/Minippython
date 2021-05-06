import flask
from flask import Flask, jsonify, request
import sqlite3
import json
 
# Creation  d'un Web App
 
app = Flask(__name__)
app.config["DEBUG"] = True
 
# Creation d'un Blockchain
 
class Blockchain(object):
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.blocks = []

bchain=Blockchain(4)

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d
 
 
 

 
@app.route('/bloc/all', methods = ['GET'])
 
def all_bloc():
    conn = sqlite3.connect('blockchainDB.db')

    conn.row_factory = dict_factory
    
    cur = conn.cursor()

    all_bloc = cur.execute('SELECT * FROM Bloc;').fetchall()

    return jsonify(all_bloc)
 
@app.route('/bloc', methods=['POST'])

def add_bloc():
    conn = sqlite3.connect('blockchainDB.db')

    sql = '''INSERT INTO books(index, previousHash, timestamp, data, hash,nonce)
                VALUES(?,?,?,?,?) '''
                
    cur = conn.cursor()

    body = request.get_json()

    data = json.loads(json.dumps(body))
    blockchainDB = (data['index'], data['previousHash'], data['timestamp'], data['data'], data['hash'],data['nonce'])

    cur.execute(sql, blockchainDB)

    conn.commit()

    return resp


 
@app.route('/bloc', methods=['GET'])
def api_filter():
    query_parameters = request.args

    index = query_parameters.get('index')
    previousHash= query_parameters.get('previousHash')
    timestamp = query_parameters.get('timestamp')
    data = query_parameters.get('data')
    hash = query_parameters.get('hash')
    nonce = query_parameters.get('nonce')


    query = "SELECT * FROM bloc WHERE"
    to_filter = []

    if index:
        query += ' index=? AND'
        to_filter.append(index)
    if previousHash:
        query += ' previousHash=? AND'
        to_filter.append(previousHash)
    if timestamp:
        query += ' timestamp=? AND'
        to_filter.append(timestamp)
    if data:
        query += ' data=? AND'
        to_filter.append(data)
    if hash:
        query += ' hash=? AND'
        to_filter.append(hash)
    if nonce:
        query += 'nonce =? AND'
        to_filter.append(nonce)
    if not (index or previousHash or  timestamp or data or hash or nonce):
        return page_not_found(404)

    query = query[:-4] + ';'

    conn = sqlite3.connect('blockchainDB.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()

    results = cur.execute(query, to_filter).fetchall()

    return jsonify(results)

app.run()
 
 
