#!/usr/bin/env python3

import tarfile
import os
import posixpath
import datetime
import boto3
import sys
import settings

docroot = sys.argv[1]


for directory in os.listdir(docroot):

  dt = datetime.datetime.now()

  ts = "{}-{}-{}".format(dt.day,dt.month,dt.year)
  
########################################## Creating tar.gz file ######################################
  tar_name = '/website_backup/{}-{}.tar.gz'.format(directory,ts)
  
  absPath = posixpath.join(docroot,directory)
  
  tar = tarfile.open(tar_name,'w:gz')

  upload_name = 'website_backup/{}-{}.tar.gz'.format(directory,ts)
  
  tar.add(absPath)
  
  tar.close()

########################################## Creating Session ##########################################
  session = boto3.Session(
  aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
  aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY
  )

  s3 = session.resource('s3')
  
########################################## upload backup file to s3 ####################################

  s3.Bucket(settings.BUCKET_NAME).upload_file(tar_name,upload_name)

  res ='The backup of website {} has been uploaded to s3 bucket {}'.format(directory,settings.BUCKET_NAME)
  print (res)
  
########################################## Remove backupfile from local directory #########################

  os.remove(tar_name)
  print ("Backup has been removed from local directory")
  
