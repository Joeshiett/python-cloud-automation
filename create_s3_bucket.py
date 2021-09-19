import boto3
import logging
from botocore.exceptions import ClientError

s3 = boto3.client('s3')

# Using default region configured in local machine with access key 
def createBucket(bucket_name):
    try:
        s3.create_bucket(Bucket=bucket_name)
        print('Done!')
    except ClientError as e:
        logging.error(e)
        print('oops! something is wrong, maybe your internet connection?')

# Specifying region 
def create_bucket_with_region(bucket_name, region):
    try:
        s3 = boto3.client('s3', region_name=region)
        location = {'LocationConstraint': region}
        s3.create_bucket(Bucket=bucket_name,
                         CreateBucketConfiguration=location)
        print('Done!')
    except ClientError as e:
        logging.error(e)
        print('oops! something is wrong, maybe your internet connection?')  

while True:
    prompt = input('Do you wish to create an S3 bucket? Y or N?\n')
    if prompt.upper() == 'Y':
        another_prompt = input('Do you wish to specify region of bucket? Y or N?\n')
        if another_prompt.upper() == 'Y':
            user_input = input('Specify bucket name (Name must be unique!):\n')
            specify_region = input('specify region:\n')
            create_bucket_with_region(user_input, specify_region)
        elif another_prompt.upper() == 'N':
            user_input = input('Specify bucket name (Name must be unique!):\n')
            createBucket(user_input)
    elif prompt.upper() == 'N':
        print('Alright goodbye...')
    break


              