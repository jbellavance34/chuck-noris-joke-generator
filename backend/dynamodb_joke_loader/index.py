#!/usr/bin/env python
# script to load jokes in dynamodb table

import json
import boto3

TABLE_NAME = 'chuck-noris-jokes'

def load_jokes(id, joke, table_name):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table_name)
    response = table.put_item(
        Item={
            'id': id,
            'joke': joke
            }
    )


if __name__ == '__main__':
    with open("jokes.txt") as file:
        id = 1
        for line in file:
            print('Loading joke id ' + str(id) + ' in dynamodb')
            load_jokes(id, line, TABLE_NAME)
            id = id + 1

