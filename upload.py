import boto3
import os


# Create an S3 client
client = boto3.client('s3')

#set variable for bucket name
bucket_name = 'countai-knitting-field-datastorage'
# file = os.listdir(os.getcwd()+"/data/")[0]
file = "manifest.json"
cur_path = os.getcwd()+"/data/"+file


#upload file to s3 bucket
client.upload_file(cur_path, bucket_name, file)