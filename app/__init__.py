import boto3

import app.key_config as keys

dynamodb = boto3.resource('dynamodb')

dynamodb_client = boto3.client('dynamodb')
