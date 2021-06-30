import os
import urllib
import json
import boto3

def get_token_for_team(team):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('token')
    response = table.get_item(
        Key={
            'team_id': team
        }
    )
    return response['Item']["token"]

def is_bot(event):
    return 'bot_profile' in event['event']

def send_response(event, response_text):
    SLACK_URL = "https://slack.com/api/chat.postEphemeral" # use postMessage if we want visible for everybody
    channel_id = event["event"]["channel"]
    user = event["event"]["user"]
    team_id = event["team_id"]
    bot_token = get_token_for_team(team_id)
    data = urllib.parse.urlencode({
            "token": bot_token,
            "channel": channel_id,
            "text": response_text,
            "user": user,
            "link_names": True
        })
    data = data.encode("ascii")
    request = urllib.request.Request(SLACK_URL, data=data, method="POST")
    request.add_header( "Content-Type", "application/x-www-form-urlencoded" )
    res = urllib.request.urlopen(request).read()
    print('res:', res)


def lambda_handler(event, context):
    event = json.loads(event["body"])
    if not is_bot(event):
        message = "Hello world !"
        send_response(event, message)
    
    return {
        'statusCode': 200,
        'body': 'OK'
    }