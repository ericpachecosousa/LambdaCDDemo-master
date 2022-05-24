import boto
import json
##teste
##teste

ec2 = boto.client('ec2')
def lambda_handler(event, context):
    response = ec2.describe_availability_zones()
    return {"statusCode": 200, "body": json.dumps(response)}
