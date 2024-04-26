import sys
from langchain_aws import ChatBedrock

llm = ChatBedrock(
  model_id="anthropic.claude-3-haiku-20240307-v1:0",
  region_name='us-west-2'
)

response = llm.invoke(sys.argv[1])
print(response)