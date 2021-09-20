import boto3
from botocore.exceptions import ClientError
import logging

# Display available buckets
def display_available_buckets():
    try:
        x = 0
        s3 = boto3.resource('s3')
        for bucket in s3.buckets.all():
            x += 1
            print(f'{x}. {bucket.name}')
    except ClientError as e:
        logging.error(e)
        print('Error')

# Delete specific bucket as long as it is empty
def delete_s3_bucket(bucket_name):
    try:
        s3 = boto3.client('s3')
        s3.delete_bucket(Bucket=bucket_name)
    except ClientError as e:
        logging.error(e)
        print('Error')

# Display resources in bucket
def display_resources_in_bucket():
    user_input = input('Enter bucket name:\n')
    s3 = boto3.resource('s3')
    my_bucket = s3.Bucket(user_input)
    for file in my_bucket.objects.all():
        print(file.key)

def delete_content_bucket():
    

# Deletes empty bucket only
# delete_s3_bucket('joeshiett-bucket3')
# display_available_buckets()
# display_resources_in_bucket()