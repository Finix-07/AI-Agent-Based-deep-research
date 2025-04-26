import os
import time
import asyncio
import logging
from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate

# Configure logging for the agent
logger = logging.getLogger(__name__)
handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

class DraftingAgent:
    """
    Agent that generates structured answers from research output using Ollama LLM.

    Features:
    - Configurable model parameters (model name, temperature, max_length).
    - Built-in retries with exponential backoff on errors.
    - Synchronous and asynchronous draft methods.
    - Structured logging of calls and errors.
    """
    def __init__(
        self,
        model: str = "llama3.2",
        temperature: float = 0.7,
        max_length: int = 512,
        retries: int = 3,
        backoff: float = 2.0,
        api_url: str = "http://127.0.0.1:11434"
    ):
        # Initialize the Ollama LLM client
        self.llm = Ollama(
            model=model,
            base_url=api_url
        )

        # Define the prompt template
        template = """
You are an expert researcher. Given the following search output:

{search_output}

Write a clear, structured, markdown-formatted and proper spacing answer with:
1. A concise summary.
2. Numbered key points.
3. A "Sources" section listing the URLs used.

NOTE: 
1) Keep everything to the point and avoid unnecessary details.
2) Must use bullets and proper spacing in between sections.
3) Give URLs in the answer for only the "Sources" section.
4) Do not include any extra information or disclaimers.

"""
# (Strictly Dont include any markdown formatting anywhere)
        self.prompt = PromptTemplate(
            input_variables=["search_output"],
            template=template
        )
        
        self.retries = retries
        self.backoff = backoff

    def draft(self, search_output: str) -> str:
        """
        Formats the prompt and generates a response synchronously.
        Retries on failure with exponential backoff.
        """
        formatted = self.prompt.format(search_output=search_output)
        attempt = 0
        while attempt < self.retries:
            try:
                logger.info(f"DraftingAgent attempt {attempt + 1}")
                response = self.llm(formatted)
                return response
            except Exception as e:
                logger.warning(f"DraftingAgent failed attempt {attempt + 1}: {e}")
                attempt += 1
                time.sleep(self.backoff ** attempt)
        logger.error("DraftingAgent exceeded max retries.")
        raise RuntimeError("Maximum retries exceeded in DraftingAgent.draft")

    async def adraft(self, search_output: str) -> str:
        """
        Formats the prompt and generates a response asynchronously.
        Retries on failure with exponential backoff.
        """
        formatted = self.prompt.format(search_output=search_output)
        attempt = 0
        while attempt < self.retries:
            try:
                logger.info(f"Async DraftingAgent attempt {attempt + 1}")
                # Using apredict for async calls
                response = await self.llm.apredict(formatted)
                return response
            except Exception as e:
                logger.warning(f"Async DraftingAgent failed attempt {attempt + 1}: {e}")
                attempt += 1
                await asyncio.sleep(self.backoff ** attempt)
        logger.error("Async DraftingAgent exceeded max retries.")
        raise RuntimeError("Maximum retries exceeded in DraftingAgent.adraft")
    

if __name__ == "__main__":
    # Example usage of the DraftingAgent
    agent = DraftingAgent()
    search_output = """
    1. Python is a versatile programming language.
    2. It is widely used in web development, data science, and automation.
    3. Python has a large community and extensive libraries.
    """
    try:
        response = agent.draft(search_output)
        print("Drafted Response:")
        print(response)
    except Exception as e:
        logger.error(f"Error during drafting: {e}")