# https://www.youtube.com/watch?v=sSkj0C62mpw

import boto3
import json
from botocore.exceptions import ClientError

bedrock = boto3.client(service_name="bedrock-runtime", region_name='us-west-2')

modelId = "anthropic.claude-3-opus-20240229-v1:0"

accept = "application/json"
contentType = "application/json"

prompt = "こんにちは、あなたは誰ですか？"

request_body = {
    "anthropic_version": "bedrock-2023-05-31",
    "max_tokens": 2048,
    "messages": [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": prompt,
                },
            ],
        }
    ],
}

try:
    response = bedrock.invoke_model(
        modelId=modelId,
        body=json.dumps(request_body),
    )

    # Process and print the response
    result = json.loads(response.get("body").read())
    input_tokens = result["usage"]["input_tokens"]
    output_tokens = result["usage"]["output_tokens"]
    output_list = result.get("content", [])

    for output in output_list:
        print(output["text"])

except ClientError as err:
    print(
        "Couldn't invoke Claude 3. Here's why: %s: %s",
        err.response["Error"]["Code"],
        err.response["Error"]["Message"],
    )
    raise