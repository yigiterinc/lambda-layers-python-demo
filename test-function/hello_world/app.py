import json
import os
from db_commons.model import Person
from shared_utils.a import func1

def lambda_handler(event, context):

    print(os.listdir("/opt/python/db-schema"))
    func1()

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
            # "location": ip.text.replace("\n", "")
        }),
    }
