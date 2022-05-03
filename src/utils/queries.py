from configs.database import DATABASE_NAME, TABLE_NAMES
from utils.database import execute_statement
from utils.formatting import Formattor

def get_all_timestamp_value_data(table_name, key_name):
    query = f'''select * from {DATABASE_NAME}.{table_name};'''
    response = execute_statement(query, [])
    result = response['records']

    return Formattor().formatted_all_timestamp_value_entries(result, key_name)

def get_latest_timestamp_value_data(table_name, key_name):
    query = f'''select * from {DATABASE_NAME}.{table_name};'''
    response = execute_statement(query, [])
    result = response['records']

    return Formattor().formatted_latest_timestamp_value_entry(result, key_name)

def get_open_positions_data():
    query = f'''select * from {DATABASE_NAME}.{TABLE_NAMES.open_positions};'''
    response = execute_statement(query, [])
    result = response['records']

    out = [ row[0]['stringValue'] for row in result]

    return out