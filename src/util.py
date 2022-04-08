import os
import boto3
import mysql.connector as mysql
from dotenv import load_dotenv

load_dotenv()

DATABASE_NAME = 'protected-moonshots-activity'
HISTORIC_REWARDS_TABLE_NAME = 'historic_rewards'

rds_client = boto3.client(
    'rds-data', 
    region_name='ap-south-1', 
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