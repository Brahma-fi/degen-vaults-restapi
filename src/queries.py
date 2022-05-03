from configs.database import DATABASE_NAME, TABLE_NAMES
from database import buffer_values_row_formatter, execute_statement, historic_rewards_row_formatter

def get_historic_rewards_data():
    query = f'''select * from {DATABASE_NAME}.{TABLE_NAMES.historic_rewards};'''
    response = execute_statement(query, [])
    result = response['records']

    out = [historic_rewards_row_formatter(row) for row in result]

    return out

def get_latest_buffer_value():
    query = f'''select * from {DATABASE_NAME}.{TABLE_NAMES.buffer_values};'''
    response = execute_statement(query, [])
    result = response['records']

    out = [buffer_values_row_formatter(row) for row in result]

    return out