import boto3

import app.key_config as keys

dynamodb = boto3.resource('dynamodb',
                          aws_access_key_id=keys.ACCESS_KEY_ID,
                          aws_secret_access_key=keys.ACCESS_SECRET_KEY, 
                          region_name='us-west-2',
                          endpoint_url="http://localhost:8000")

dynamodb_client = boto3.client('dynamodb',
                          aws_access_key_id=keys.ACCESS_KEY_ID,
                          aws_secret_access_key=keys.ACCESS_SECRET_KEY, 
                          region_name='us-west-2',
                          endpoint_url="http://localhost:8000")