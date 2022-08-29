import json
import boto3

client = boto3.client('dynamodb')

def handler(event, _):

    print("Function started")
    
    existing_tables = client.list_tables()['TableNames']

    for table in existing_tables:
        print(table)

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
        },
        "body": json.dumps(existing_tables, indent=4),
    }