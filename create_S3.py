#!/usr/bin/python

# This is the Dockerfile that creates a custom image, which create a s3 bucket
# and upload a file into that bucket.

import boto3
import sys
import os

# If you're using this script to create a custom docker image then use OS level
# environment vars commented out below instead of sysparm arguments.
# Note: All environment vars will be a stored in a separate file.
# bucketname=sys.argv[1]
# filename = sys.argv[2]

file = os.environ['FILE_NAME']

#Note: It's not possible to access any files that're in local host from within
# a docker container, so create a folder in the local host environment and
# mount that folder from within docker conatiner

upload_dir = '/opt/upload_files/'
filename = upload_dir + file
print filename

#Use the below statements to accept the access key and secrete key as environment
# variables
ACCESS_KEY = os.environ('ACCESS_KEY')
SECRET_KEY = os.environ('SECRET_KEY')

#s3= boto3.resource('s3')
#Note: we can use the below statement if we have to pass the credentials.
s3 = boto3.resource('s3',aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
s3.create_bucket(
    ACL='private',
    Bucket=pms_s3,
    CreateBucketConfiguration={
        'LocationConstraint': 'us-east-2'
    }
)
# s3.meta.client.upload_file(filename, 'pms-s3', filename)
def s3_upload():
    try:
        s3.meta.client.upload_file(filename, 'pms-s3', file)
        print file + "uploaded to S3"
    except:
        none

def main():
    s3_upload()

    if __name__ == '__main__':
        sys.exit(main())
