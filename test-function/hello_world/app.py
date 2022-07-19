import json
import os
from commons.utils import func1
from db_commons.model import person

def lambda_handler(event, context):

    print(os.listdir("/opt/python/db_commons"))
    func1()

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
            # "location": ip.text.replace("\n", "")
        }),
    }
