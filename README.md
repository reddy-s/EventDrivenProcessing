# Event Driven Processing
Event driven processing can be achieved for both streaming and batch data sources. This repo aims to explain the concepts
from a practical standpoint.

## Resources:
* [Serverless.com]
* [AWS Services]
  * [Lambda]
  * [S3]
  * [Event Bridge]
  * [Cloudformation]
  * [Cloud Watch]
  * [Tracing: XRay]

## Concepts: Good To Know
* [Serverless]
* [Messaging vs Streaming]
* [Poll vs Push]
* [Event driven architectures]
* [Idempotency]
* [ACID]
* [Data lake and Lake house]

## Commands

*To deploy*
```shell
sls deploy --stage dev --aws-profile training 
```

*To Remove / delete*
```shell
sls remove --stage dev --aws-profile training 
```