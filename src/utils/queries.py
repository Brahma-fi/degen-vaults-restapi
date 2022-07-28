from ..configs.vaults import MonitoredTokenInfo
from ..configs.response import RESPONSE_KEYS
from ..configs.database import ACTIVITY_DB, PMUSDC_DB, TABLE_NAMES
from ..utils.database import InstantiatedDB
from ..utils.formatting import Formattor

class Queries():
    def __query_all_data(self, table_name):
        query = f'''select * from {ACTIVITY_DB}.{table_name};'''
        response = InstantiatedDB.execute_statement(query, [])
        result = response['records']

        return result

    def __query_latest_data(self, table_name):
        query = f'''select * from {ACTIVITY_DB}.{table_name} order by timestamp desc limit 1;'''
        response = InstantiatedDB.execute_statement(query, [])
        result = response['records']

        return result

    def get_all_timestamp_value_data(self, table_name, key_name):
        return Formattor().formatted_all_timestamp_value_entries(
            self.__query_all_data(table_name), 
            key_name
        )

    def get_latest_timestamp_value_data(self, table_name, key_name, index=-1):
        return Formattor().formatted_latest_timestamp_value_entry(
            self.__query_latest_data(table_name), 
            key_name,
            index
        )

    def get_latest_timestamp_data(self, table_name, key_name, type, index):
        rows = self.__query_latest_data(table_name)

        if len(rows) == 0:
            return {}
            
        timestamp = rows[-1][0]['stringValue']
        value = rows[-1][index][type]

        result = {}
        result[RESPONSE_KEYS.timestamp] = timestamp
        result[key_name] = value

        return result

    def get_open_positions_data(self):
        out = [ row[0]['stringValue'] for row in self.__query_all_data(TABLE_NAMES.open_positions)]

        return out

    def get_withdraw_slippage(self, token: MonitoredTokenInfo):
        query = f'''select slippage from {ACTIVITY_DB}.{token.table}'''
        response = InstantiatedDB.execute_statement(query, [])
        data = response['records']

        result = {}
        result[RESPONSE_KEYS.slippage] = data[-1][0]['doubleValue']

        return result

    def get_pool_health(self, pool):
        query = f'select * from {PMUSDC_DB}.{TABLE_NAMES.stablecoin_health} where pool_name = \'{pool}\' order by timestamp desc limit 1'
        response = InstantiatedDB.execute_statement(query,[],True)
        data = response['records']

        result = {}
        result[RESPONSE_KEYS.health] = data[0][7]['stringValue']

        return result

    def get_pool_apy(self, pool):
        query = f'select * from {PMUSDC_DB}.{TABLE_NAMES.basepool_apy} where pool_name = \'{pool}\' order by timestamp desc limit 1'
        response = InstantiatedDB.execute_statement(query,[],True)
        data = response['records']

        result = {}
        result[RESPONSE_KEYS.apy] = data[0][1]['doubleValue']

        return result