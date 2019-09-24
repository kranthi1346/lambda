import boto3
import json

ec2 = boto3.client('ec2')
def lambda_handler(event, context, callback) => {
    callback(null, { statusCode: 200, body: 'Hello from Lambda' });
};

    response = ec2.describe_availability_zones()
    return {"statusCode": 200, "body": json.dumps(response)}
