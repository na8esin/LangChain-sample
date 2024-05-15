import os
from langchain_community.agent_toolkits import create_sql_agent, SQLDatabaseToolkit
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

toolkit = SQLDatabaseToolkit(db=db, llm=llm, use_query_checker=True)

agent_executor = create_sql_agent(
  llm, toolkit=toolkit, verbose=True, handle_parsing_errors=True
)

response = agent_executor.invoke(
    {"input": "productsの件数は? 説明文は不要です。"}
)
print("-----------------------------")
print(response)
print("-----------------------------")
