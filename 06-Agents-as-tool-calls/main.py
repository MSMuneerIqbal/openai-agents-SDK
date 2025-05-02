from agents import Agent, Runner, set_tracing_disabled, AsyncOpenAI, OpenAIChatCompletionsModel
from dotenv import load_dotenv
import os
set_tracing_disabled(True)
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client = external_client
)

# Define a shopping assistant agent
shopping_agent = Agent(
    name="Shopping Assistant",
    instructions="You assist users in finding products and making purchase decisions.",
    model=model
)

# Define a support agent
support_agent = Agent(
    name="Support Agent",
    instructions="You help users with post-purchase support and returns.",
    model=model
)


# Convert agents into tools
shopping_tool = shopping_agent.as_tool(
    tool_name="Shopping_Assistant_Tool",
    tool_description="A tool to assist users in finding products and making purchase decisions."
)
support_tool = support_agent.as_tool(
    tool_name="Support_Agent_Tool",
    tool_description="A tool to help users with post-purchase support and returns."
)

# Define a triage agent that delegates tasks
triage_agent = Agent(
    name="Triage Agent",
    instructions="You route user queries to the appropriate department.",
    tools=[shopping_tool, support_tool],
    model=model
)

# Run the triage agent with a sample inputs
result = Runner.run_sync(triage_agent, "I need help with a recent purchase.")
print(result.final_output)