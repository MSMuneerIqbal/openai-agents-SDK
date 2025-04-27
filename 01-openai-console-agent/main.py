# Console Chat Agent
# Imports
import os
from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI, set_tracing_disabled
from dotenv import load_dotenv, find_dotenv

set_tracing_disabled(True)

_: bool = load_dotenv(find_dotenv())  # Find .env file

gemini_key = os.getenv("GEMINI_API_KEY")

# Provider
gemini_provider = AsyncOpenAI(
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    api_key=gemini_key
)

# Model
gemini_model = OpenAIChatCompletionsModel(
    model="gemini-1.5-flash",
    openai_client=gemini_provider
)

# Agent
greeting_agent = Agent(
    name="Greeting Agent",
    model=gemini_model,
    instructions="""
    You are a helpful assistant that greets the user.
    """
)

#  Create Console Agent that take input, continues
#    chat in the loop till user Exits
# While Loop -> loop input ....
# For Loop -> loop input ....
def main():
    history = []
    # [{"role": "user", "content": "?"}, {"role": "assistant", "content": ""}]
    while True:
        # Input
        user_input = input("Enter your message. Type 'exit' to quit: ")
        
        if user_input.lower() == "exit":
            print("Exiting...")
            break
        
        history.append({"role": "user", "content": user_input})

        # Agent Loop
        response = Runner.run_sync(
            starting_agent=greeting_agent,
            input=history
        )

        history.append({"role": "assistant", "content": response.final_output})

        print("assistant: ", response.final_output)


main()