
# -*- coding: utf-8 -*-


import sys
import traceback
import ibm_boto3
import ibm_db
from ibm_botocore.client import Config, ClientError
from datetime import datetime, timedelta, timezone
import re


def main():
    print("helen-testing-functions-456")
    
    try:
        read_xlsx_inst = Readxlsx(dict)
        file_list = read_xlsx_inst.get_file_list()
        read_xlsx_inst.exec_file_list(file_list)
        print("Finished the program.")
    except SystemExit as e:
        print("Logging: Exit the program. As a testing.")
        #return { 'message' : 'Returned: Exit the program. As a testing.'}
    return { 'message' : 'python implemention finished'}



