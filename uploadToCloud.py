import boto3
import pathlib
import os
class Upload:
  def __init__(self, bucketName, objectName, fileName):
    self.s3 = boto3.client("s3")
    self.bucketName = bucketName
    self.objectName = objectName
    self.fileName = fileName

  def uploadFile(self):
    print("Uploading File {0} to Bucket = {1} with ObjectName = {2}".format(self.fileName, self.bucketName, self.objectName))
    response = self.s3.upload_file(self.fileName, self.bucketName, self.objectName)
    print(response)  # return None or Error if Error




