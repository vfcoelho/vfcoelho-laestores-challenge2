

def execute(event,context):
    print(event)
    return {
                "headers": {
                    "Access-Control-Allow-Origin": "*",
                    "content-type": "application/json"
                },
                "statusCode": 200,
                "body":{"test":"successful"}
            }