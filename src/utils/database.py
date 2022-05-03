import os
import boto3
from dotenv import load_dotenv

from configs.database import DATABASE_NAME

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