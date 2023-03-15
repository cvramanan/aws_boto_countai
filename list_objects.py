import boto3
import os



# Create an S3 client
client = boto3.client('s3')

#set variable for bucket name
bucket_name = 'countai-cone360-uvinspection-data'



#list all files in bucket
allObjects = client.list_objects(Bucket=bucket_name)
for obj in allObjects['Contents']:
    print(obj['Key'])