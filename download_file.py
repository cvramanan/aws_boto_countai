import boto3
import os



# Create an S3 client
client = boto3.client('s3')

#set variable for bucket name
bucket_name = 'countai-cone360-uvinspection-data'
saveLocation = os.getcwd()+"/downloads/"

#download file from s3 bucket
client.download_file(bucket_name, Key='1678430054.4439335.png', Filename= saveLocation+'1678430054.4439335.png')

#list downloaded files
print(os.listdir(saveLocation))
