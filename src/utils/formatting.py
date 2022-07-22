from flask import jsonify
from ..configs.response import RESPONSE_KEYS

class Formattor():
    def __get_timestamp_value_result(self,timestamp, value, key_name):
        result = {}
        result[RESPONSE_KEYS.timestamp] = timestamp
        result[key_name] = value

        return result

    def __timestamp_key_row_formatter(self, row, key_name):
        timestamp = row[0]['stringValue']
        value = row[1]['doubleValue']

        return self.__get_timestamp_value_result(timestamp, value, key_name)

    def formatted_all_timestamp_value_entries(self, rows, key_name):
        return [self.__timestamp_key_row_formatter(row, key_name) for row in rows]

    def formatted_latest_timestamp_value_entry(self, rows, key_name):
        if len(rows) == 0:
            return {}
            
        timestamp = rows[-1][0]['stringValue']
        value = rows[-1][1]['doubleValue']

        return self.__get_timestamp_value_result(timestamp, value, key_name)

    def formatted_response(self, status_code, result):
        return (jsonify(data = result), status_code, {"ContentType": 'application/json'})