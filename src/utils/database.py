import os
import boto3
from dotenv import load_dotenv

from configs.database import ACTIVITY_DB, PMUSDC_DB

class Database():
    def __init__(self):
        load_dotenv()

        self.rds_client_v1 = boto3.client(
            'rds-data', 
            region_name='us-east-2', 
            aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID"),
            aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
        )

        self.rds_client_v2 = boto3.client(
            'rds-data', 
            region_name='us-east-2', 
            aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID_V2"),
            aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY_V2")
        )
    
    def execute_statement(self, query, params, is_v2 = False):
        rds_client = self.rds_client_v2 if is_v2 else self.rds_client_v1
        database = PMUSDC_DB if is_v2 else ACTIVITY_DB
        secret_arn = os.getenv('DB_SECRET_ARN_V2') if is_v2 else os.getenv('DB_SECRET_ARN')
        resource_arn = os.getenv('DB_ARN_V2') if is_v2 else os.getenv('DB_ARN')

        response = rds_client.execute_statement(
            secretArn = secret_arn,
            resourceArn = resource_arn,
            database = database,
            sql = query,
            parameters = params) 
        return response

InstantiatedDB = Database()