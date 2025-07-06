
from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    symbol = request.json.get('symbol', 'XAUUSD')
    prediction = random.choice(['Buy', 'Sell'])
    pip_target = random.randint(20, 100)
    return jsonify({
        'symbol': symbol,
        'prediction': prediction,
        'pip_target': pip_target,
        'timeframe': 'M15'
    })

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    if data.get('username') == 'admin' and data.get('password') == 'Predictor#1':
        return jsonify({'status': 'success'})
    return jsonify({'status': 'failed'}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
