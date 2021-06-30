import json
import base64
from urllib.parse import parse_qs

def lambda_handler(event, context):
    event = base64.b64decode(event["body"])
    event = parse_qs(event.decode("utf-8"))

    print('Slash command called with params: ', event)

    return {
        'statusCode': 200,
        'body': 'OK'
    }
