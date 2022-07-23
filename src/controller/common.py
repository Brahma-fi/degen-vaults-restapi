from ..utils.on_chain import OnChainQueries
from ..utils.queries import Queries
from ..utils.formatting import Formattor

from ..configs.vaults import MONITORED_TOKENS, VAULTS
from ..configs.database import TABLE_NAMES
from ..configs.response import RESPONSE_KEYS

def get_tvl():
    result = OnChainQueries().get_tvl()
    return Formattor().formatted_response(200, result)

def get_open_positions():
    result = Queries().get_open_positions_data()
    return  Formattor().formatted_response(200, result)

def get_all_buffers():
    result = Queries().get_all_timestamp_value_data(TABLE_NAMES.buffer_values, RESPONSE_KEYS.buffer)
    return  Formattor().formatted_response(200, result)

def get_latest_usdc_balance():
    result = Queries().get_latest_timestamp_value_data(TABLE_NAMES.usdc_balances, RESPONSE_KEYS.value,1)
    return  Formattor().formatted_response(200, result)

def get_latest_position():
    result = Queries().get_latest_timestamp_data(TABLE_NAMES.usdc_balances, RESPONSE_KEYS.position, 'stringValue', -1)
    return  Formattor().formatted_response(200, result)

def get_latest_buffer():
    result = Queries().get_latest_timestamp_value_data(TABLE_NAMES.buffer_values, RESPONSE_KEYS.buffer)
    return  Formattor().formatted_response(200, result)

def get_historic_rewards():
    frax_output = Queries().get_latest_timestamp_value_data(
        TABLE_NAMES.historic_rewards, 
        RESPONSE_KEYS.claimed_rewards
    )
    susd_output = Queries().get_latest_timestamp_value_data(
        TABLE_NAMES.susd_rewards,
        RESPONSE_KEYS.claimed_rewards
    )
    result = susd_output[RESPONSE_KEYS.claimed_rewards]+frax_output[RESPONSE_KEYS.claimed_rewards]
    return  Formattor().formatted_response(200, result)