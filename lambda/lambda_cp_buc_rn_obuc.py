"""
-*- coding: utf-8 -*-
========================
AWS Lambda
========================
Contributor: Chirag Rathod (Srce Cde)
========================
"""

import boto3
from pprint import pprint
def lambda_handler(event, context):
    s3 = boto3.resource("s3")
    source_bucket = "sbucket-name"
    destination_bucket = "dbucket-name"

    for obj in source_bucket.objects.all():
        destination_bucket_file_rename = obj.key + str("_new")
        s3.Object(dest_b.name,dest_filename).copy_from(CopySource= { 'Bucket': obj.bucket_name , 'Key' : obj.key})
    
    return 'Thanks'
