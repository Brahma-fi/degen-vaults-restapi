from ..configs.response import RESPONSE_KEYS
from ..configs.database import DATABASE_NAME, TABLE_NAMES, MonitoredTokenInfo
from ..utils.database import InstantiatedDB
from ..utils.formatting import Formattor

class Queries():
    def __query_all_data(self, table_name):
        query = f'''select * from {DATABASE_NAME}.{table_name};'''
        response = InstantiatedDB.execute_statement(query, [])
        result = response['records']

        return result

    def get_all_timestamp_value_data(self, table_name, key_name):
        return Formattor().formatted_all_timestamp_value_entries(
            self.__query_all_data(table_name), 
            key_name
        )

    def get_latest_timestamp_value_data(self, table_name, key_name):
        return Formattor().formatted_latest_timestamp_value_entry(
            self.__query_all_data(table_name), 
            key_name
        )

    def get_open_positions_data(self):
        out = [ row[0]['stringValue'] for row in self.__query_all_data(TABLE_NAMES.open_positions)]

        return out

    def get_withdraw_slippage(self, token: MonitoredTokenInfo):
        query = f'''select slippage from {DATABASE_NAME}.{token.table}'''
        response = InstantiatedDB.execute_statement(query, [])
        data = response['records']

        result = {}
        result[RESPONSE_KEYS.slippage] = data[-1][0]['doubleValue']

        return result