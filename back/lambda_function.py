def lambda_handler(event: any, context: any):
    user = event["user"]
    message = 'Hello' + user