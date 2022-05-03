import os
import boto3
from dotenv import load_dotenv

from configs.database import DATABASE_NAME
from configs.response import RESPONSE_KEYS

load_dotenv()

rds_client = boto3.client(
    'rds-data', 
    region_name='us-east-2', 
    aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
)
 
def execute_statement(query, params):
    response = rds_client.execute_statement(
        secretArn = os.getenv('DB_SECRET_ARN'),
        resourceArn = os.getenv('DB_ARN'),
        database = DATABASE_NAME,
        sql = query,
        parameters = params) 
    return response

def get_timestamp_value_result(timestamp, value, key_name):
    result = {}
    result[RESPONSE_KEYS.timestamp] = timestamp
    result[key_name] = value

    return result

def timestamp_key_row_formatter(row, key_name):
    timestamp = row[0]['stringValue']
    value = row[1]['doubleValue']

    return get_timestamp_value_result(timestamp, value, key_name)

def formatted_latest_timestamp_value_entry(rows, key_name):
    timestamp = rows[-1][0]['stringValue']
    value = rows[-1][-1]['doubleValue']

    return get_timestamp_value_result(timestamp, value, key_name)