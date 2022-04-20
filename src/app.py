from flask_cors import CORS
from flask import Flask, jsonify
from src.queries import get_historic_rewards_data, get_open_positions_data, get_share_price_data

app = Flask(__name__)
CORS(app)

@app.route("/", methods=['GET'])
def health_check():
    return {'status':'OK'}

@app.route("/historic_rewards", methods=['GET'])
def get_historic_rewards():
    result = get_historic_rewards_data()
    return  (jsonify(data = result), 200, {"ContentType": 'application/json'})


@app.route("/open_timestamps", methods=['GET'])
def get_open_positions():
    result = get_open_positions_data()
    return  (jsonify(data = result), 200, {"ContentType": 'application/json'})


@app.route("/share_price", methods=['GET'])
def get_share_prices():
    result = get_share_price_data()
    return  (jsonify(data = result), 200, {"ContentType": 'application/json'})


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080)