import os
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel,set_tracing_disabled
from dotenv import load_dotenv
load_dotenv()
set_tracing_disabled(True)
gemini_api_key = os.getenv("GOOGLE_API_KEY")
#Reference: https://ai.google.dev/gemini-api/docs/openai
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)
# Agent
web_agent = Agent(
    name="website developer",
    instructions="you are a full stack website developer. solve user web related queries",
    model=model,
    handoff_description="Specialized in web development"
)
# Agent
mobile_agent = Agent(
    name="mobile app developer",
    instructions="you are specialized in mobile application development. solve user mobile dev related queries",
    model=model,
    handoff_description="Specialized in mobile development"
)

# Agent
# agent as tools
devops_agent = Agent(
    name="devops",
    instructions="you are dev ops developer. solve user dev ops related queries",
    model=model
)

openai_agent = Agent(
    name="openai agent", # Changed the name to openai_agent
    instructions="you are a openai agentic developer. solve user dev ops related queries",
    model=model
)
agentai = Agent(
    name="Agentic Ai",
    instructions= "You are openai agentic and devops engineer give answer to use tools only",
    tools=[devops_agent.as_tool(
        tool_name="devops",
        tool_description="you are dev ops developer. solve user dev ops related queries"
    )
    ,
    openai_agent.as_tool(
        tool_name="openai_agent",
        tool_description="you are a openai agentic developer. solve user dev ops related queries"
    )
    ],
    model=model
)
# Triage Agent Handoff Agent
panacloud_agent = Agent(
    name="Triage Agent",
    instructions= "you are a triage agent you will handoff to agents related queries dnt ask user just handoffs",
    handoffs=[web_agent,mobile_agent,agentai],
    model=model
)

# Test Search Agent
response = Runner.run_sync(panacloud_agent, "Give Road map of devops engineer")
print(response.final_output)
print(response.last_agent.name)