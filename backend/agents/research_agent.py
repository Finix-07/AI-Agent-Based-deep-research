import os
from langchain.tools import BaseTool
from tavily import TavilyClient
from dotenv import load_dotenv

load_dotenv()

tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

class ResearchAgent(BaseTool):

    name: str = "ResearchAgent"
    description: str = "A research agent that can answer questions using the Tavily API."

    def _run(self, query: str) -> str:
        response = tavily_client.search(query)
        return response["results"][0]['content'] if response["results"] else "No results found."

    async def _arun(self, query: str) -> str:
        raise NotImplementedError("ResearchAgent does not support async run.")
    

if __name__ == "__main__":
    agent = ResearchAgent()
    query = "What is the capital of France?"
    result = agent._run(query)
    print(f"Query: {query}\n\nResult: {result}")
