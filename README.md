# snapshotalyzer-30000
Project to Manage AWS EBS Snapshots. 


## About

This project uses boto3 to manage EC2 instances and EBS Snapshots. 

## Configuration

shotty uses the configuration file created by the AWS CLI for e.g

`aws configure --profile shotty`

## Running

`pipenv run python shotty/shotty.py <command> <sub-command> <--project=PROJECT>"`

*command* is instances, volumes, or snapshots
*sub-command* - depends on command
*project* is optional
