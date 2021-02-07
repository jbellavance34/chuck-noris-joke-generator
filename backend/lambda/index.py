#!/usr/bin/env python
# backend api code to generate chuck-noris-jokes

import boto3
import random
import json
import os 

TABLE_NAME = os.getenv('TABLE_NAME')

def get_random_joke(id, table_name):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table_name)
    response = table.get_item(
            Key={
                'id' : id,
            }
        )
    return response['Item']

def handler(event, context):
    random_id = random.randint(1, 100)
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "joke": get_random_joke(random_id,TABLE_NAME)
    }
