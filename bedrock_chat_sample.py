from langchain_community.chat_models import BedrockChat

llm = BedrockChat(
  model_id="anthropic.claude-3-opus-20240229-v1:0",
  region_name='us-west-2'
)

response = llm.invoke("how can langsmith help with testing?")
print(response)