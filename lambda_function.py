import json
import boto3
from time import gmtime, strftime

def add_question_to_db(event):
    username = event['username']
    userid = event['userid']
    questiontext = event['questiontext']
    
    now = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
    print(now)
    
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('q-and-a-page')
    
    response = table.put_item(
        Item={
            'userid': userid,
            'username': username,
            'questiontext': questiontext,
            'time': now
            })
            
    print(response)
    

def lambda_handler(event, context):
    add_question_to_db(event)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
