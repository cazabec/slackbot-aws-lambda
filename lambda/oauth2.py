import os
import urllib
import json
import boto3

def save_token_to_dynamo(response):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('token')
    table.put_item(
        Item={
            'team_id': response["team"]["id"],
            'token': response["access_token"]
        }
    )

def lambda_handler(event, context):
    print('Event received:', event)
    
    code = event['queryStringParameters']['code']
    
    data = urllib.parse.urlencode({
            "client_id": os.environ["CLIENT_ID"],
            "client_secret": os.environ["CLIENT_SECRET"],
            "code": code
        })
    data = data.encode("ascii")
    
    request = urllib.request.Request("https://slack.com/api/oauth.v2.access", data=data, method="POST")
    request.add_header( "Content-Type", "application/x-www-form-urlencoded" )
    response = urllib.request.urlopen(request).read()
    response = response.decode("utf-8")
    response = json.loads(response)
    save_token_to_dynamo(response)
    return {
        'statusCode': 200,
        'body': 'OK',
        "headers": {
            'Content-Type': 'text/html',
        }
    }
