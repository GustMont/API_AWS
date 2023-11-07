import json

def authenticate(event):
    if 'headers' in event and 'Authorization' in event['headers']:
        valid_token = "Token1234"
        if event['headers']['Authorization'] == f"Bearer {valid_token}":
            return True
    return False

def lambda_handler(event, context):
    if not authenticate(event):
        return {
            'statusCode': 401,
            'body': json.dumps({'message': 'Autenticação falhou'})
        }
    return {
        'statusCode': 200,
        'body': json.dumps(event['body'])
    }