def handler(event, context):
    userID = event["userID"]
    Token = event["Token"]

    # Any logic that your app should perform.

    return {
        "statusCode": 200,
        "body": "Hello there",
        "userID" : userID,
        "Token": Token
    }
