import traceback
import uuid
from logging import exception
from flask import (Blueprint, current_app, jsonify, request)

from app import dynamodb, dynamodb_client

api = Blueprint('api', __name__, url_prefix='/user')

table = dynamodb.Table('users')

@api.route('/health', methods=['GET', ])
def get_health():
    return jsonify(status='healthy')

#api to access: /user/token?username= (GET call)
@api.route('/token', methods=['GET', 'POST'])
def token():
    try:
        if request.method == 'POST':
            content_type = request.headers.get('Content-Type')
            if (content_type == 'application/json'):
                post_data = request.json
                username = post_data['username']
            result = table.get_item(Key={'username': username})
            data = result.get('Item')
            if data:
                return jsonify(message='user already created')
                       
            # Save data in DynamoDb table
            token  = uuid.uuid4().hex
            response = table.put_item(Item={'username': username, 'token' : token})
            return jsonify({'message': 'user created', 'token' : token})
        
        username = request.args.get('username')
        if not username:
            return jsonify(message='username not passed')
        result = table.get_item(Key={'username': username})
        data = result.get('Item')

        if data is None:
            return jsonify({'message': 'No user found'})
        
        return jsonify(credentails=data)
    except Exception as ex:
        return jsonify(exception = traceback.print_exc())

@api.route('/tables', methods=['GET'])
def get_tables():
    
    existing_tables = dynamodb_client.list_tables()['TableNames']
    if existing_tables is None:
        return jsonify({'message': 'No table found'})
    return jsonify(tables = existing_tables)
