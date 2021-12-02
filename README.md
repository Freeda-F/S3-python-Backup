# S3-python-Backup

Simple Python backup script for backing up files into S3 bucket.

## Requirements

- IAM user with S3 Full access
- S3 bucket for storing backup
- Python
- Boto3

## Modules used 

- boto3
- os
- posixpath
- sys
- tarfile

## Installation

1. Install the below dependencies to use the script
```
yum install -y git
yum install -y python3
yum install -y python3-pip
```
2. This script requires boto, to install boto simply 
```
pip3 install boto3
```

## Configuration

```
git clone https://github.com/Freeda-F/S3-python-Backup.git
cd S3-python-Backup
python3 backup-script-s3.py /var/www/ or ./backup-script-s3.py /var/www/
```
Note : Make sure to change the parameters in the settings.py file to your IAM credentials and bucket name.

## Result

After executing this script, you will have the backup of the directories in .tar.gz file format in your S3 Bucket. 

