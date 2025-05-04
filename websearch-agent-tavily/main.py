from agents.tool import function_tool
from tavily import TavilyClient
import os
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel,set_tracing_disabled
from dotenv import load_dotenv
set_tracing_disabled(True)
load_dotenv()  # Load environment variables from .env file
gemini_api_key = os.getenv("GEMINI_API_KEY")
if gemini_api_key is None:  
    raise ValueError("GEMINI_API_KEY environment variable is not set.")
search_api_key = os.getenv("TAVILY_API_KEY")

#Reference: https://ai.google.dev/gemini-api/docs/openai
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

"""# Create tools"""

@function_tool("search_online")
def xyz(query: str):
  """Search online for the given query."""
  tavily_client = TavilyClient(api_key=search_api_key)
  response = tavily_client.search(query)
  return response

"""# Connect tools with Agent"""

import asyncio

agent = Agent(
    name="SearchAssistant",
    instructions="You can search online or simply answer. Response with an Emoji",
    tools=[xyz], # add tools here
    model=model
)

result = Runner.run_sync(agent, "call search tool and tell what is the todays dollar to pkr price rate")
print(result.final_output)
