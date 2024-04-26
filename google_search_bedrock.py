# https://qiita.com/cyberBOSE/items/a331ed830ed1859a198d
# https://python.langchain.com/docs/modules/agents/agent_types/xml_agent/

import sys
from langchain import hub
from langchain_aws import ChatBedrock
from langchain.agents import create_xml_agent
from langchain.agents.agent import AgentExecutor
from langchain.agents import Tool
from langchain_google_community import GoogleSearchAPIWrapper
from dotenv import load_dotenv

load_dotenv()

# google検索apiのラッパー
# 環境変数として、GOOGLE_CSE_ID, GOOGLE_API_KEYが必要
# GOOGLE_API_KEYは無料のfirebaseプロジェクトでも取得可能
search = GoogleSearchAPIWrapper()

# プロンプトのテンプレート
prompt = hub.pull("hwchase17/xml-agent-convo")

# 使用可能なツールと説明
tools = [
    Tool(
        name="google_search",
        description="Search Google for recent results.",
        func=search.run,
    ),
]

llm = ChatBedrock(
  model_id="anthropic.claude-3-haiku-20240307-v1:0",
  region_name='us-west-2'
)

agent = create_xml_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True, handle_parsing_errors=True)

# Agentの実行
answer = agent_executor.invoke({"input": sys.argv[1]})
print(answer['output'])
