from langchain_google_community import GoogleSearchAPIWrapper
from langchain_core.tools import Tool
from dotenv import load_dotenv

load_dotenv()

search = GoogleSearchAPIWrapper()

tool = Tool(
    name="google_search",
    description="Search Google for recent results.",
    func=search.run,
)

response = tool.run("今日の日本のニュースは?")
print(response)
