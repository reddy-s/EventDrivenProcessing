import json
import boto3
import os

from uuid import uuid4


def fun(event, context):
    records = event.get("Records")
    client = boto3.client('events')
    publish_status = []
    for record in records:
        s3_payload = record.get("s3")
        correlation_id = str(uuid4())
        payload = {"correlation_id": correlation_id, "s3": s3_payload}
        status = client.put_events(
            Entries=[
                {
                    'Source': os.environ.get("EVENT_SOURCE"),
                    'DetailType': os.environ.get("EVENT_DETAIL_TYPE"),
                    'Detail': json.dumps(payload),
                    'EventBusName': os.environ.get("EVENT_BUS"),
                    'TraceHeader': correlation_id
                },
            ]
        )
        publish_status.append(status)
        print(f"processed event and added trace id: {correlation_id}")

    response = {"statusCode": 200, "body": json.dumps(publish_status)}
    return response
