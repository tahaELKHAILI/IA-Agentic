import os
from dotenv import load_dotenv

from langchain.agents import AgentState, create_agent
from langchain.tools import tool, ToolRuntime
from langgraph.types import Command
from langchain.messages import ToolMessage
from langgraph.checkpoint.memory import InMemorySaver
from langchain_ollama import ChatOllama
from langchain.messages import HumanMessage


load_dotenv()
# Part 5: Définir un état personnalisé d’agent en héritant de AgentState

class CustomState(AgentState):
    favourite_colour:str

# Part 6: Agent qui modifie un état

@tool
def update_favourite_colour(favourite_colour:str, runtime: ToolRuntime) -> Command:
    """Update the favourite colour of the user in the state once they've revealed it."""
    return Command(update={
        "favourite_colour": favourite_colour,
        "messages": [ToolMessage("Successfully updated favourite colour", 
                                 tool_call_id = runtime.tool_call_id)]
    }
    )

model_name = os.getenv("MODEL_OLLAMA")
llm = ChatOllama(model=model_name, temperature=0)

agent = create_agent(model=llm,
                     checkpointer= InMemorySaver(),
                     tools=[update_favourite_colour],
                     state_schema=CustomState)

response = agent.invoke(
{ "messages": [HumanMessage(content="My favourite colour is green")]},
{"configurable": {"thread_id": "1"}}
)
print(response['messages'][-1].content)

# Part 7: Agent qui récupère un état

@tool
def read_favourite_colour(runtime:ToolRuntime) -> str:
    """ Read the favourite colour of the user from the state """
    try:
        return runtime.state["favourite_colour"]
    except:
        return "No favourite colour found in state"
    

agent = create_agent(
    model=llm,
    tools=[update_favourite_colour, read_favourite_colour],
    checkpointer=InMemorySaver(),
    state_schema=CustomState
)

response = agent.invoke(
    { "messages": [HumanMessage(content="My favourite colour is green")]},
    {"configurable": {"thread_id": "1"}}
)
print(response['messages'][-1].content)

response = agent.invoke(
    { "messages": [HumanMessage(content="What's my favourite colour?")]},
    {"configurable": {"thread_id": "1"}}
)
print(response['messages'][-1].content)