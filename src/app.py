from flask_cors import CORS
from flask import Flask

from .utils.on_chain import OnChainQueries
from .configs.database import MONITORED_TOKENS, TABLE_NAMES, VAULTS
from .configs.response import RESPONSE_KEYS
from .utils.formatting import Formattor
from .utils.queries import Queries

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
    return  Formattor().formatted_response(200, result)

@app.route("/latest_buffer", methods=['GET'])
def get_latest_buffer():
    result = Queries().get_latest_timestamp_value_data(TABLE_NAMES.buffer_values, RESPONSE_KEYS.buffer)
    return  Formattor().formatted_response(200, result)

@app.route("/latest_balance", methods=['GET'])
def get_latest_usdc_balance():
    result = Queries().get_latest_timestamp_value_data(TABLE_NAMES.usdc_balances, RESPONSE_KEYS.value)
    return  Formattor().formatted_response(200, result)

@app.route("/all_buffers", methods=['GET'])
def get_all_buffers():
    result = Queries().get_all_timestamp_value_data(TABLE_NAMES.buffer_values, RESPONSE_KEYS.buffer)
    return  Formattor().formatted_response(200, result)

@app.route("/open_timestamps", methods=['GET'])
def get_open_positions():
    result = Queries().get_open_positions_data()
    return  Formattor().formatted_response(200, result)

@app.route("/<vault_name>/share_price", methods=['GET'])
def get_share_prices(vault_name):
    if not(VAULTS.is_valid_vault(vault_name=vault_name)):
        return Formattor().formatted_response(400,{
            'error': f"{vault_name} :: is not a valid vault name"
        })

    result = Queries().get_all_timestamp_value_data(
        TABLE_NAMES.share_price_db 
        if vault_name == VAULTS.pmusdc.name else 
        TABLE_NAMES.ethmaxi_share_price_db, 
        RESPONSE_KEYS.price
    )
    return  Formattor().formatted_response(200, result)

@app.route("/<vault_name>/apr", methods=['GET'])
def get_apr_values(vault_name):
    if not(VAULTS.is_valid_vault(vault_name=vault_name)):
        return Formattor().formatted_response(400,{
            'error': f"{vault_name} :: is not a valid vault name"
        })

    result = Queries().get_latest_timestamp_value_data(
        TABLE_NAMES.share_price_db 
        if vault_name == VAULTS.pmusdc.name else 
        TABLE_NAMES.ethmaxi_share_price_db, 
        RESPONSE_KEYS.apr
    )
    return  Formattor().formatted_response(200, result)

@app.route("/<token_name>/slippage", methods=['GET'])
def get_slippage(token_name):
    if not(MONITORED_TOKENS.is_valid_token(token_name=token_name)):
        return Formattor().formatted_response(400,{
            'error': f"{token_name} :: is not a valid vault name"
        })

    result = Queries().get_withdraw_slippage(
        MONITORED_TOKENS.frax if token_name == MONITORED_TOKENS.frax.name else MONITORED_TOKENS.steth
    )
    return  Formattor().formatted_response(200, result)

@app.route("/tvl", methods=['GET'])
def get_tvl():
    result = OnChainQueries().get_tvl()
    return Formattor().formatted_response(200, result)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080)