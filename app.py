from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)

CORS(app)


def quantity(sku):
    return 3


@app.route('/availability/<sku>', methods=['GET'])
def availability(sku):
    data = dict(sku=sku, quantity=quantity(sku))
    return jsonify(data), 200
