import requests
from flask import Flask, jsonify, request
from flask_cors import  CORS

app = Flask(__name__)

CORS(app, resources={r"/api/*": {"origins" : "*"}})
search = []

@app.route('/api/', methods=['POST'])
def post_request():
    data = request.get_json()
    search.append(data["site"])
    return jsonify({"Request": "Success!!!"}), 201

@app.route('/api/', methods=['GET'])
def get_request():
    if not search:
        return jsonify({"Request": "Bad Request!!!"}), 400
    data = requests.get(search[0])
    cep_data = data.json()
    return jsonify(cep_data), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)