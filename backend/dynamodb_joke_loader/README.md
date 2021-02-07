# Dynamodb joke loader

Script to load jokes in dynamodb table

# Initial configuration 

- create the dynamodb table

    - name: chuck-noris-jokes
    - primary key: 
        - hash: id
        - type: number

# Requirements

- dynamodb:putItem permission


# Loading joke steps
- Connect to you aws account
- run the script
    ```python
    python index.py 
    Loading joke id 1 in dynamodb
    Loading joke id 2 in dynamodb
    Loading joke id 3 in dynamodb
    Loading joke id 4 in dynamodb
    Loading joke id 5 in dynamodb
    Loading joke id 6 in dynamodb
    Loading joke id 7 in dynamodb
    Loading joke id 8 in dynamodb
    Loading joke id 9 in dynamodb
    (...)
    ```