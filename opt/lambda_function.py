import json
import os
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

import boto3

DATABASE = os.environ['DATABASE']
TABLE_NAME = os.environ['TABLE_NAME']

def lambda_handler(event, context):
    logger.info("backup取得開始")
    dynamodb_client = boto3.client(DATABASE)
    res = dynamodb_client.create_backup(
        TableName = TABLE_NAME,          # テーブル名
        BackupName  = TABLE_NAME + '_bk' # バックアップファイル名
    )
    logger.info(res)

    return {
        'statusCode': 200,
        'body': json.dumps('backup取得完了')
    }