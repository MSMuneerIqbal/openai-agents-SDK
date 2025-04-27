import os
import chainlit as cl  # import complete module
from agents import Agent, Runner, OpenAIChatCompletionsModel, set_tracing_disabled, AsyncOpenAI
from dotenv import load_dotenv, find_dotenv

_: bool = load_dotenv(find_dotenv())

# Provider
gemini_provider = AsyncOpenAI(
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    api_key=os.getenv("GEMINI_API_KEY")
)

# Agent
greeting_agent = Agent(
    name="Greeting Agent",
    instructions="You are a helpful assistant that greets the user.",
    model=OpenAIChatCompletionsModel(
        model="gemini-1.5-flash", openai_client=gemini_provider)
)

# Agent Loop


@cl.on_message
async def main(message: cl.Message):
    # Your custom logic goes here...
    ai_response = await Runner.run(starting_agent=greeting_agent, input=message.content)

    # Send a response back to the user
    await cl.Message(
        content=ai_response.final_output,
    ).send()