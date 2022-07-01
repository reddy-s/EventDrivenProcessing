import json
import boto3

from uuid import uuid4


def fun(event, context):
    records = event.get("Records")
    client = boto3.client('events')
    publish_status = []
    for record in records:
        s3_payload = record.get("s3")
        correlation_id = str(uuid4())
        payload = {
            "correllationId": correlation_id,
            "s3": s3_payload
        }
        status = client.put_events(
            Entries=[
                {
                    'Source': 'ObjectLandedEventPublisher',
                    'DetailType': 'ObjectLandedEvent',
                    'Detail': json.dumps(payload),
                    'EventBusName': 'MLPlatformDataArrivedEventBus',
                    'TraceHeader': correlation_id
                },
            ]
        )
        publish_status.append(status)
    print(event)

    response = {
        "statusCode": 200,
        "body": json.dumps(publish_status)
    }
    print(response)

    return response

