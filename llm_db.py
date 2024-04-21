from langchain_community.chat_models import BedrockChat
from langchain.chains import create_sql_query_chain
from langchain_community.utilities import SQLDatabase

import os
from dotenv import load_dotenv

load_dotenv()

db = SQLDatabase.from_uri(f'mysql://root:@127.0.0.1:3309/{os.environ['DB_NAME']}')

llm = BedrockChat(
  model_id="anthropic.claude-3-opus-20240229-v1:0",
  region_name='us-west-2',
  credentials_profile_name=os.environ['AWS_PROFILE']
)

chain = create_sql_query_chain(llm, db)
response = chain.invoke({"question": "How many products are there. Please respond only sql. No explanation is necessary."})

# プロンプトの内容を確認したい場合
# chain.get_prompts()[0].pretty_print()

# print(response)

result = db.run(response)
print(result)
