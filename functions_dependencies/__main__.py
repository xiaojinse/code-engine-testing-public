
# -*- coding: utf-8 -*-


import sys
import traceback
import ibm_boto3
import ibm_db
from ibm_botocore.client import Config, ClientError
from datetime import datetime, timedelta, timezone
import re



def main():
    print("helen-testing-function-123")
    name = params.get("name", "world")
    greeting = "Hello " + name + "!"
    
    return {
        "headers": {
            "Content-Type": "application/json",
        },
        "statusCode": 200,
        "body": greeting,
    }

