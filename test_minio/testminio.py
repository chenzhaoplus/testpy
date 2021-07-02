#!/usr/bin/env/env python3
import boto3

s3 = boto3.client('s3',
                  endpoint_url='http://172.16.4.85:9000',
                  aws_access_key_id='AKIAIOSFODNN7EXAMPLE',
                  aws_secret_access_key='wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY',
                  region_name='us-east-1')

r = s3.select_object_content(
    Bucket='zzstatic',
    Key='test.json',
    ExpressionType='SQL',
    Expression="SELECT * FROM S3Object[*].Rules[*]",
    InputSerialization={
        'CompressionType': 'NONE',
        'JSON': {
            'Type': 'DOCUMENT'
        }
    },
    OutputSerialization={'JSON': {}},
)

for event in r['Payload']:
    if 'Records' in event:
        records = event['Records']['Payload'].decode('utf-8')
        print(records)
    elif 'Stats' in event:
        statsDetails = event['Stats']['Details']
        print("Stats details bytesScanned: ")
        print(statsDetails['BytesScanned'])
        print("Stats details bytesProcessed: ")
        print(statsDetails['BytesProcessed'])
