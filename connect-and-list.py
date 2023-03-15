import boto3

# Create an S3 client
client = boto3.client('s3')

#retrieve all buckets Metadata
response = client.list_buckets()

#loop through all buckets data and print bucket name
for bucket in response['Buckets']:
    print(bucket['Name'])
    