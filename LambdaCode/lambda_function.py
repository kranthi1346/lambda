import boto3
import json
    def lambdaTest(event, context)
        response = {}
        dummybody = {'body':'something'}
        response['statusCode'] = 200
        response['body'] = dummybody
        response["headers"] = {"Content-Type": "application/json"},
        return json.dumps(response)
