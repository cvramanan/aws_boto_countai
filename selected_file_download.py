import boto3
import os
from halo import Halo


#remote folder 
remoteFolder = "scm-pailung/2023-03-28/HD/100/"



# Create an S3 client
client = boto3.client('s3')

#set variable for bucket name
bucket_name = 'countai-knitting-field-datastorage'

saveLocation = os.getcwd()+"/downloadedFieldData/"

#create directory to save downloaded files
os.makedirs(saveLocation, exist_ok=True)



#list all files in bucket
s3r = boto3.resource('s3')
bucket = s3r.Bucket(bucket_name)




splitRatioConstant = 1

print(bucket.objects.filter(Prefix=remoteFolder))

with Halo(text='Counting files', spinner='dots',color="cyan") as spinner:
    count = 0
    for i in bucket.objects.filter(Prefix=remoteFolder):
        count += 1
        if count%1000 == 0:
            spinner.text = "Counting files: "+str(count)
    splitRatioConstant = count//5000
    spinner.succeed("Total files in Remote location: "+str(count) + " Split Ratio: "+str(splitRatioConstant))

splitRatioConstant = count//5000

# exit()


with Halo(text='Copying files', spinner='dots',color="cyan") as spinner:
    for i,object_summary in  enumerate(bucket.objects.filter(Prefix=remoteFolder)):
        if i%splitRatioConstant != 0:
            continue
        # print(object_summary.key)
        dir = object_summary.key.split("/")
        dir = dir[:-1]
        dir = "/".join(dir)
        os.makedirs(saveLocation+(dir), exist_ok=True)
        client.download_file(bucket_name, Key=object_summary.key, Filename = saveLocation+object_summary.key)
        if i%10 == 0:
            spinner.text = "Copying files: "+str(i)
    spinner.succeed("Total files Copied: "+str(i))
