from database import BUFFER_VALUES_TABLE_NAME, buffer_values_row_formatter, execute_statement, historic_rewards_row_formatter, DATABASE_NAME, HISTORIC_REWARDS_TABLE_NAME

def get_historic_rewards_data():
    query = f'''select * from {DATABASE_NAME}.{HISTORIC_REWARDS_TABLE_NAME};'''
    response = execute_statement(query, [])
    result = response['records']

    out = [historic_rewards_row_formatter(row) for row in result]

    return out

def get_latest_buffer_value():
    query = f'''select * from {DATABASE_NAME}.{BUFFER_VALUES_TABLE_NAME};'''
    response = execute_statement(query, [])
    result = response['records']

    out = [buffer_values_row_formatter(row) for row in result]

    return out