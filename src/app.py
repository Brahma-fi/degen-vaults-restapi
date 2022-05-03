from flask_cors import CORS
from flask import Flask, jsonify
from configs.database import TABLE_NAMES
from configs.response import RESPONSE_KEYS
from utils.queries import Queries

app = Flask(__name__)
CORS(app)

@app.route("/", methods=['GET'])
def health_check():
    return {'status':'OK'}

@app.route("/historic_rewards", methods=['GET'])
def get_historic_rewards():
    result = Queries().get_all_timestamp_value_data(
        TABLE_NAMES.historic_rewards, 
        RESPONSE_KEYS.claimed_rewards
    )
    return  (jsonify(data = result), 200, {"ContentType": 'application/json'})

@app.route("/latest_buffer", methods=['GET'])
def get_latest_buffer():
    result = Queries().get_all_timestamp_value_data(TABLE_NAMES.buffer_values, RESPONSE_KEYS.buffer)
    return  (jsonify(data = result), 200, {"ContentType": 'application/json'})

@app.route("/open_timestamps", methods=['GET'])
def get_open_positions():
    result = Queries().get_open_positions_data()
    return  (jsonify(data = result), 200, {"ContentType": 'application/json'})


@app.route("/share_price", methods=['GET'])
def get_share_prices():
    result = Queries().get_all_timestamp_value_data(TABLE_NAMES.share_price_db, RESPONSE_KEYS.price)
    return  (jsonify(data = result), 200, {"ContentType": 'application/json'})

@app.route("/apr", methods=['GET'])
def get_apr_values():
    result = Queries().get_latest_timestamp_value_data(TABLE_NAMES.share_price_db, RESPONSE_KEYS.apr)
    return  (jsonify(data = result), 200, {"ContentType": 'application/json'})



if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080)