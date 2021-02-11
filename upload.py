"""
AWS S3 Uploader Script
======================
Modified: 2021-02

This script uploads files to AWS S3.
"""

import os
import logging
import boto3

# bind logging to config file
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(threadName)s %(name)s %(message)s"
)

target_file = os.environ['TARGET_FILE']
bucket = os.environ['BUCKET']
obj = os.environ['OBJECT']

logging.info("S3 uploader script")
logging.info("------------------")
logging.info("File: %s", target_file)
logging.info("Bucket: %s", bucket)

s3 = boto3.client(
    "s3",
    aws_access_key_id=os.environ['ACCESS_ID'],
    aws_secret_access_key=os.environ['ACCESS_KEY']
)
with open(target_file, "rb") as f:
    s3.upload_fileobj(f, bucket, obj)

logging.info("S3 upload complete.")