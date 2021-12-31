import traceback
import uuid
from logging import exception
from flask import (Blueprint, current_app, jsonify, request)

from app import dynamodb

api = Blueprint('api', __name__, url_prefix='/user')

table = dynamodb.Table('users')

@api.route('/health', methods=['GET', ])
def get_health():
    return jsonify(status='healthy')

@api.route('/<string:username>', methods=['GET', 'POST'])
def get_token(username):
    try:
        # existing_tables = dynamodb.list_tables()['TableNames']
        # if table_name not in existing_tables:
        #     raise Exception('table not found')
        
        result = table.get_item(Key={'username': username})
        data = result.get('Item')
            
        if request.method == 'POST':
            # check if user is not present 
            if data:
                return jsonify({'message': 'user already created'})
            # Save data in DynamoDb table
            token  = uuid.uuid4().hex
            response = table.put_item(Item={'username': username, 'token' : token})
            return jsonify({'message': 'user created', 'token' : token})
            
        if data is None:
            return jsonify({'message': 'No user found'})
        return jsonify(credentails=result.get('Item'))
    except Exception as ex:
        print(traceback.print_exc())

@api.route('/tables', methods=['GET'])
def get_tables():
    
    existing_tables = dynamodb.list_tables()['TableNames']
    if existing_tables is not None:
        return jsonify({'message': 'No table found'})
    return jsonify(existing_tables)
                   
