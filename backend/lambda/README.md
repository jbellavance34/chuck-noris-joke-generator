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

- create api gw 

    - name: chuck-noris-joke-apigw
    - type: REST API
    - endpoint type: regional
    - method for / path 
        - GET
            - integration type: lambda function
            - lambda function: chuck-noris-joke-generator
        - OPTIONS (made with option 'Enable CORS')
            - integration type: MOCK
            - Method response
                - headers
                    - Access-Control-Allow-Headers: Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token
                    - Access-Control-Allow-Methods: GET,OPTIONS
                    - Access-Control-Allow-Origin: *
    - stage
        - prod

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
- Create api gw with the configuration section
- test the invoke url 
    ```bash
    curl -s https://wbeu2sfdkk.execute-api.ca-central-1.amazonaws.com/prod |jq -r 
    {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "joke": {
            "id": 44,
            "joke": "    Chuck Norris can play the violin with a piano.\n"
        }
    }
    ```