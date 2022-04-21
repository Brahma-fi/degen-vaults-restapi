from src.database import execute_statement, row_formatter, DATABASE_NAME, HISTORIC_REWARDS_TABLE_NAME, OPEN_POSITION_TABLE_NAME, SHARE_TABLE_NAME

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

def get_share_price_data():
    query = f'''select * from {DATABASE_NAME}.{SHARE_TABLE_NAME};'''
    response = execute_statement(query, [])
    result = response['records']
    out = [ {'timestamp': row[0]['stringValue'], 'price': row[1]['doubleValue']} for row in result]
    return out

def get_apr_data():
    query = f'''select * from {DATABASE_NAME}.{SHARE_TABLE_NAME};'''
    response = execute_statement(query, [])
    result = response['records']
    timestamp = result[-1][0]['stringValue']
    apr = result[-1][-1]['doubleValue']
    return {'timestamp': timestamp, 'apr': apr}  