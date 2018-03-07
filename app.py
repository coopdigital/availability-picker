from flask import Flask, jsonify, request
from flask_cors import CORS
import random
import json

app = Flask(__name__)

CORS(app)


def quantity(sku):
    return random.randint(-1, 10)


@app.route('/availability', methods=['POST'])
def availability():
    skus = json.loads(request.data.decode('utf-8'))['skus']
    data = list(map(lambda sku: {'sku': sku, 'quantity': quantity(sku)}, skus))
    return jsonify(data), 200
