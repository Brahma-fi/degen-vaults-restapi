from configs.database import DATABASE_NAME, TABLE_NAMES
from configs.response import RESPONSE_KEYS
from utils.database import formatted_latest_timestamp_value_entry, timestamp_key_row_formatter,execute_statement

def get_historic_rewards_data():
    query = f'''select * from {DATABASE_NAME}.{TABLE_NAMES.historic_rewards};'''
    response = execute_statement(query, [])
    result = response['records']

    out = [timestamp_key_row_formatter(row, RESPONSE_KEYS.claimed_rewards) for row in result]

    return out

def get_latest_buffer_value():
    query = f'''select * from {DATABASE_NAME}.{TABLE_NAMES.buffer_values};'''
    response = execute_statement(query, [])
    result = response['records']

    return formatted_latest_timestamp_value_entry(result, RESPONSE_KEYS.buffer)

def get_open_positions_data():
    query = f'''select * from {DATABASE_NAME}.{TABLE_NAMES.open_positions};'''
    response = execute_statement(query, [])
    result = response['records']

    out = [ row[0]['stringValue'] for row in result]

    return out

def get_share_price_data():
    query = f'''select * from {DATABASE_NAME}.{TABLE_NAMES.share_price_db};'''
    response = execute_statement(query, [])
    result = response['records']

    out = [ timestamp_key_row_formatter(row, RESPONSE_KEYS.price) for row in result]

    return out

def get_apr_data():
    query = f'''select * from {DATABASE_NAME}.{TABLE_NAMES.share_price_db};'''
    response = execute_statement(query, [])
    result = response['records']

    return formatted_latest_timestamp_value_entry(result, RESPONSE_KEYS.apr)