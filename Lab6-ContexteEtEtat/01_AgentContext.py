import os
from dotenv import load_dotenv

from dataclasses import dataclass
from langchain_ollama import ChatOllama
from langchain.agents import create_agent
from langchain.messages import HumanMessage
from langchain.tools import tool, ToolRuntime


# Context class
@dataclass
class ColourContext:
    favourite_colour:str = "Red"
    least_favourite_colour: str = "Green"


# Agent without context
load_dotenv()

model_name = os.getenv("MODEL_OLLAMA")
llm = ChatOllama(model=model_name, temperature=0)
agent = create_agent(model=llm, context_schema=ColourContext)

response = agent.invoke({
    "messages":[HumanMessage(content="What is my favourite colour?")]
}, context=ColourContext())

print("--Response of an agent with no access to context--")
print(response["messages"][-1].content)

# Agent with access to context
# Tools allow us to access context
@tool
def get_favourite_colour(runtime: ToolRuntime) -> str:
    """ Get the favourite colour of the user"""
    return runtime.context.favourite_colour

@tool
def get_least_favourite_colour(runtime: ToolRuntime) -> str:
    """ get the least favourite colour of the user"""
    return runtime.context.least_favourite_colour

agent = create_agent(model=llm,
                     tools=[get_favourite_colour, get_least_favourite_colour],
                     context_schema=ColourContext)


response = agent.invoke({
    "messages": [HumanMessage(content="What is my favourit colour ?")]
}, context=ColourContext())

print("--Response of an agent with access to context--")
print(response["messages"][-1].content)

# Change in context

response = agent.invoke(
    {"messages": [HumanMessage(content="What is my favourite colour?")]},
    context=ColourContext(favourite_colour="blue")
)
print(response['messages'][-1].content)


#==========================================================
# Creating my own version for practice
#==========================================================

#Creating context
@dataclass
class MusicContext:
    favourite_band :str = "Metallica"
    favourite_genre :str = "Metal"
    least_favourite_genre : str = "Pop"

#Crating the tools
@tool
def get_favourite_band(runtime: ToolRuntime)-> str:
    """Get the favrourite band of the user"""
    return runtime.context.favourite_band

@tool
def get_favourite_genre(runtime: ToolRuntime)-> str:
    """Get the favrourite genre of the user"""
    return runtime.context.favourite_genre

@tool
def get_least_favourite_genre(runtime: ToolRuntime)-> str:
    """Get the least favrourite genre of the user"""
    return runtime.context.least_favourite_genre

#Creating the agent
music_agent = create_agent(model=llm,
                           tools=[get_favourite_band, get_favourite_genre, get_least_favourite_genre],
                           context_schema=MusicContext)

answer = music_agent.invoke(
    {"messages": [HumanMessage(content="What is my favourite genre?")]},
    context=MusicContext()
    )

print("--Response of an agent with access to music context--")
print(answer["messages"][-1].content)