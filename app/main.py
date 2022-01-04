from flask import Flask, jsonify
from app.config import app_config
import boto3

from app.routes import api as api_blueprint
from app import dynamodb, dynamodb_client


def create_app(config_name):   
    app = Flask(__name__, instance_relative_config=True)    
    
    # Load config based on environment
    app.config.from_object(app_config[config_name])
    # app.config.from_pyfile('config.py')
    
    try:
        table_name = 'users'
        existing_tables = dynamodb_client.list_tables()['TableNames']
        if table_name not in existing_tables:
            table = dynamodb.create_table(
                TableName='users',
                KeySchema=[{'AttributeName': 'username','KeyType': 'HASH'}],
                AttributeDefinitions=[{'AttributeName': 'username','AttributeType': 'S'}],
                ProvisionedThroughput={'ReadCapacityUnits': 1,'WriteCapacityUnits': 1})    
            
            # Wait until the table exists.
            table.meta.client.get_waiter('table_exists').wait(TableName='users')
            # Print out some data about the table.
            print('table Created, table : ',table)      
    except Exception as ex:
        return jsonify({'message': 'table not created'})

    app.register_blueprint(api_blueprint)
    return app
