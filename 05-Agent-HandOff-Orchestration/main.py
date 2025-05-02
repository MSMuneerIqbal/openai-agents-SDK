from agents import (
    AsyncOpenAI,
    OpenAIChatCompletionsModel,
    RunConfig
)
from agents import Agent, Runner, set_tracing_disabled
from dotenv import load_dotenv
import os
set_tracing_disabled(True)
load_dotenv()  # Load environment variables from .env file
gemini_api_key = os.getenv("GEMINI_API_KEY")
if gemini_api_key is None:  
    raise ValueError("GEMINI_API_KEY environment variable is not set.")

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)


model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

urdu_agent = Agent(
    name="Urdu agent",
    instructions="You are a helpful assistant that speaks Urdu.",
    model=model
)

english_agent = Agent(
    name="English agent",
    instructions="You only speak English",
    model=model
)

triage_agent = Agent(
    name="Triage agent",
    instructions="Handoff to the appropriate agent based on the language of the request.",
    handoffs=[urdu_agent, english_agent],
    model=model
)

# Run the triage agent with a sample input
result = Runner.run_sync(triage_agent, "ٓاپ کیسے ہیں؟")
print(result.final_output)