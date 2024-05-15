import os
from langchain_community.agent_toolkits import create_sql_agent
from langchain_community.utilities import SQLDatabase
from langchain_aws import ChatBedrock
from dotenv import load_dotenv

from app.utils import mysql_uri

load_dotenv()


llm = ChatBedrock(
  model_id="anthropic.claude-3-haiku-20240307-v1:0",
  region_name='us-west-2'
)

db = SQLDatabase.from_uri(mysql_uri())

agent_executor = create_sql_agent(llm, db=db, verbose=True, handle_parsing_errors=True)
# print(agent_executor.get_prompts()) # 空のリストが返ってくる

response = agent_executor.invoke(
    {"input": "Describe the schema of the products table"}
)
print(response)


# こんなエラーが出てうまくいかない
# langchain_core.exceptions.OutputParserException: Could not parse LLM output: `Question: Describe the schema of the products table
# Thought: To describe the schema of the products table, I will first need to check if the table exists in the database.
# Action: sql_db_list_tables`
# During handling of the above exception, another exception occurred:
# 中略
# raise ValueError(
# ValueError: An output parsing error occurred. In order to pass this error back to the agent and have it try again, pass `handle_parsing_errors=True` to the AgentExecutor. This is the error: Could not parse LLM output: `Question: Describe the schema of the products table
# Thought: To describe the schema of the products table, I will first need to check if the table exists in the database.
# Action: sql_db_list_tables`
