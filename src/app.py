from flask_cors import CORS
from flask import Flask, jsonify
from queries import get_historic_rewards_data

app = Flask(__name__)
CORS(app)

@app.route("/historic_rewards", methods=['GET'])
def get_historic_rewards():
    result = get_historic_rewards_data()
    return  (jsonify(data = result), 200, {"ContentType": 'application/json'})

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")