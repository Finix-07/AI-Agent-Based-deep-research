from tavily import TavilyClient
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))
response = tavily_client.search("Trending Netflix Shows")

print(response)