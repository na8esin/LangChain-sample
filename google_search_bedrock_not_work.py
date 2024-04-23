# https://python.langchain.com/docs/modules/agents/quick_start/
# うまくいかないパターン

from langchain_google_community import GoogleSearchAPIWrapper
from langchain_core.tools import Tool
from langchain_aws import ChatBedrock, BedrockLLM
from langchain_community.chat_models import BedrockChat
from langchain_community.llms import Bedrock
from langchain_core.prompts import ChatPromptTemplate
from langchain.agents import create_tool_calling_agent
from langchain.agents import AgentExecutor

from dotenv import load_dotenv

load_dotenv()

search = GoogleSearchAPIWrapper()

google_search = Tool(
    name="google_search",
    description="Search Google for recent results.",
    func=search.run,
)
tools = [google_search]

# 下記のエラーが発生する
# in bind_tools
#     raise NotImplementedError()
llm = ChatBedrock(
  model_id="anthropic.claude-3-haiku-20240307-v1:0",
  region_name='us-west-2'
)

# 下記のエラーが発生する
# in create_tool_calling_agent
#     raise ValueError(
# ValueError: This function requires a .bind_tools method be implemented on the LLM.
# llm = BedrockLLM(
#   model_id="anthropic.claude-v2:1",
#   region_name='us-west-2'
# )

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant"),
        ("placeholder", "{chat_history}"),
        ("human", "{input}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
)

agent = create_tool_calling_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
response = agent_executor.invoke({"input": "今日の日本のニュースは?"})
print(response)

