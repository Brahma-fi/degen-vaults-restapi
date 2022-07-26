from flask_cors import CORS
from flask import Flask

from .controller.common import get_all_buffers, get_historic_rewards, get_latest_balance, get_latest_buffer, get_latest_position, get_open_positions, get_tvl
from .controller.pool import get_pool_apy, get_pool_health
from .controller.vault import get_apr_values, get_share_prices, get_slippage

app = Flask(__name__)
CORS(app)

# Health check
@app.route("/", methods=['GET'])
def health_check():
    return {'status':'OK'}

# Common Stats Endpoints
app.route("/historic_rewards", methods=['GET'])(get_historic_rewards)
app.route("/latest_buffer", methods=['GET'])(get_latest_buffer)
app.route("/<token_name>/latest_balance", methods=['GET'])(get_latest_balance)
app.route("/all_buffers", methods=['GET'])(get_all_buffers)
app.route("/open_timestamps", methods=['GET'])(get_open_positions)
app.route("/latest_position", methods=['GET'])(get_latest_position)
app.route("/tvl", methods=['GET'])(get_tvl)

# Pool Endpoints
app.route("/<pool_name>/health", methods=["GET"])(get_pool_health)
app.route("/<pool_name>/apy", methods=["GET"])(get_pool_apy)

# Vault Endpoints
app.route("/<vault_name>/share_price", methods=['GET'])(get_share_prices)
app.route("/<vault_name>/apr", methods=['GET'])(get_apr_values)
app.route("/<token_name>/slippage", methods=['GET'])(get_slippage)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080)