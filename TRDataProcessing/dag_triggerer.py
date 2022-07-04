import boto3
import json
import os


def fun(event, context):
    client = boto3.client('events')
    correlation_id = event["detail"]["correlation_id"]
    status = client.put_events(
        Entries=[
            {
                'Source': os.environ.get("EVENT_SOURCE"),
                'DetailType': os.environ.get("EVENT_DETAIL_TYPE"),
                'Detail': json.dumps(event),
                'EventBusName': os.environ.get("EVENT_BUS"),
                'TraceHeader': correlation_id
            },
        ]
    )
    response = {
        "statusCode": 200,
        "body": status
    }
    print(f"[INFO] {correlation_id}: Sucessfully triggered DAG [XYZ]")

    return response
