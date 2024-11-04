from flask import Flask, request, jsonify

import requests
from hashing import get_node_for_key

app = Flask(__name__)
data_store = {}


NODES = ["http://localhost:5001", "http://localhost:5002"]

def forward_request(node, endpoint, data=None, method='PUT'):
    url = f"{node}{endpoint}"
    try:
        if method == 'PUT':
            response = requests.put(url, json=data)
        elif method == 'DELETE':
            response = requests.delete(url)
        elif method == 'GET':
            response = requests.get(url)
        return response
    except requests.exceptions.RequestException:
        return jsonify({"error": "Node unreachable"}), 500


@app.route('/store/<key>', methods=['PUT'])

def put_key(key):
    data_store[key] = request.json.get('value')
    return jsonify({"status": "success"}), 200

@app.route('/store/<key>', methods = ['GET'])
def get_key(key):
    value = data_store.get(key)
    if value is None:
        return jsonify({"error": "key not found"}), 400
    return jsonify({"value": value}), 200

@app.route('/store/<key>', methods = ['DELETE'])
def delete_key(key):
    if key in data_store:
        del data_store[key]
        return jsonify({"status":"deleted"}), 200
    return jsonify({"error":"key not found"}), 400

if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 5000
    app.config['port'] = port
    app.run(port=port)
