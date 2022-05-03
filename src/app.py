from flask_cors import CORS
from flask import Flask, jsonify
from queries import get_apr_data, get_open_positions_data, get_share_price_data
from utils.queries import get_historic_rewards_data, get_latest_buffer_value

app = Flask(__name__)
CORS(app)

@app.route("/", methods=['GET'])
def health_check():
    return {'status':'OK'}

@app.route("/historic_rewards", methods=['GET'])
def get_historic_rewards():
    result = get_historic_rewards_data()
    return  (jsonify(data = result), 200, {"ContentType": 'application/json'})

@app.route("/latest_buffer", methods=['GET'])
def get_latest_buffer():
    result = get_latest_buffer_value()
    return  (jsonify(data = result[-1] if len(result) > 0 else {}), 200, {"ContentType": 'application/json'})

@app.route("/open_timestamps", methods=['GET'])
def get_open_positions():
    result = get_open_positions_data()
    return  (jsonify(data = result), 200, {"ContentType": 'application/json'})


@app.route("/share_price", methods=['GET'])
def get_share_prices():
    result = get_share_price_data()
    return  (jsonify(data = result), 200, {"ContentType": 'application/json'})

@app.route("/apr", methods=['GET'])
def get_apr_values():
    result = get_apr_data()
    return  (jsonify(data = result), 200, {"ContentType": 'application/json'})



if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080)