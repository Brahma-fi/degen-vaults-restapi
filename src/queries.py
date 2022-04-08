import pandas as pd
from database import execute_statement, row_formatter, DATABASE_NAME, HISTORIC_REWARDS_TABLE_NAME

def get_historic_rewards_data():
    query = f'''select * from {DATABASE_NAME}.{HISTORIC_REWARDS_TABLE_NAME};'''
    result = execute_statement(query, [])

    out = [row_formatter(row) for row in result['records']]
    out = pd.DataFrame(out)

    out['timestamp'] = pd.to_datetime(out['timestamp'])
    out.sort_values(by=['timestamp'], inplace=True)

    return out