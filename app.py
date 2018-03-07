from flask import Flask, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)

CORS(app)


def quantity(sku):
    return random.randint(-1, 10)


@app.route('/availability/<sku>', methods=['GET'])
def availability(sku):
    data = dict(sku=sku, quantity=quantity(sku))
    return jsonify(data), 200
