from flask import Flask, jsonify

app = Flask(__name__)

def quantity(sku):
    return 3

@app.route('/availability/<sku>', methods=['GET'])
def availability(sku):
    data = dict(
        sku=sku,
        quantity=quantity(sku)
    )
    return jsonify(data), 200
