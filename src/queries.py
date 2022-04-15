from src.database import execute_statement, row_formatter, DATABASE_NAME, HISTORIC_REWARDS_TABLE_NAME, OPEN_POSITION_TABLE_NAME

def get_historic_rewards_data():
    query = f'''select * from {DATABASE_NAME}.{HISTORIC_REWARDS_TABLE_NAME};'''
    response = execute_statement(query, [])
    result = response['records']

    out = [row_formatter(row) for row in result]

    return out


def get_open_positions_data():
    query = f'''select * from {DATABASE_NAME}.{OPEN_POSITION_TABLE_NAME};'''
    response = execute_statement(query, [])
    result = response['records']
    out = [ row[0]['stringValue'] for row in result]

    return out