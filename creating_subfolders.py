import boto3
import os


# Create an S3 client
client = boto3.client('s3')

#set variable for bucket name
bucket_name = 'countai-cone360-uvinspection-data'

#creating subfolders
client.put_object(Bucket=bucket_name, Key='subfolder1/')
client.put_object(Bucket=bucket_name, Key='subfolder2/')

allObjects = client.list_objects(Bucket=bucket_name)
for obj in allObjects['Contents']:
    print(obj['Key'], obj['Size'], obj['LastModified'])