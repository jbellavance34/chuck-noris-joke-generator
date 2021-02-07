# Dynamodb joke api

api that gets random chuck noris jokes from dynamodb table

# Configuration 

- create lambda function

    - name: chuck-noris-joke-generator
    - iam role policies:
        - arn:aws:iam::aws:policy/AmazonDynamoDBReadOnlyAccess
        - arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole
    - runtime: python 3.8
    - environnement variables
        - TABLE_NAME: chuck-noris-joke
    - handler: lambda_function.handler

# Requirements

- dynamodb:getItem permission

# api joke installations steps

- Connect to you aws account
- Create lambda function with the configuration section
- upload the index.py code to the lambda function
- test the function
    ```python
    {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "joke": {
            "id": 93,
            "joke": "    Before he forgot a gift for Chuck Norris, Santa Claus was real.\n"
        }
    }
    ```