import boto3
import json

ec2 = boto3.client('ec2')
    response = ec2.describe_availability_zones()
    return {"statusCode": 200,"headers": { 'Content-Type': 'application/json' }, "body": json.dumps(response)}
