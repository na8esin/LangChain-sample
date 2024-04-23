from langchain_community.retrievers import WikipediaRetriever
from langchain.chains import ConversationalRetrievalChain
from langchain_aws import ChatBedrock

# 安いからhaikuを使う
model = ChatBedrock(
  model_id="anthropic.claude-3-haiku-20240307-v1:0",
  region_name='us-west-2'
)

retriever = WikipediaRetriever()
qa = ConversationalRetrievalChain.from_llm(model, retriever=retriever)

questions = [
    "こけしは何ですか？",
]

chat_history = []

for question in questions:
    result = qa({"question": question, "chat_history": chat_history})
    chat_history.append((question, result["answer"]))
    print(f"-> **Question**: {question} \n")
    print(f"**Answer**: {result['answer']} \n")
