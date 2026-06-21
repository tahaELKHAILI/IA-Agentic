import os
from dotenv import load_dotenv
from pathlib import Path

from langchain.agents import AgentState
from langchain.tools import tool, ToolRuntime
from langchain.messages import ToolMessage
from tavily import TavilyClient
from langgraph.types import Command

from src.RAG import vector_store

project_root = Path(__file__).resolve().parent.parent
load_dotenv(project_root / ".env")

# Defining the state
class ChefState(AgentState):
    preferences:list[str]


# Tools
#-------------------------------------------------
# Tool 1 = Search the RAG for the information 
# Tool 2 = Search the Web for the information
# Tool 3 = Updates the preferences
# Tool 4 = Read the preferences
#-------------------------------------------------

@tool("Search_RAG")
def Search_RAG(query: str)->str:
    """Search your local source of receipes for dishes, ingredients and cooking techniques
    args:
        query
    """
    results = vector_store.similarity_search(query)
    if not results:
        return "The local source of receipes does not contain matching receip"
    return results

@tool("Search_Web")
def Search_Web(query: str) -> str:
    """Search the web for receipes, ingredients and cooking techniques
    args"
        querry
    """
    tavily_key = os.getenv("TAVILY_API_KEY")
    if not tavily_key:
        return "Web search is unavailable. " \
        "TAVILY_API_KEY is not configuered"
    tavily_client = TavilyClient()
    return tavily_client.search(query=query)

@tool("Store_Preferences")
def Store_Preferences(preference: str, runtime: ToolRuntime) ->Command:
    """Store the user preferences in memory (likes and dislikes or diet restrictions)"""
    try:
        preferences = list(runtime.state["preferences"])
    except KeyError:
         preferences = []
    updated = preferences + [preference]

    return Command(update={
        "preferences": updated,
        "messages": [ToolMessage(
            f"Preference saved: {preference}",
            tool_call_id=runtime.tool_call_id,
        )]
    })

@tool("Get_Preferences")
def Get_Preferences(runtime: ToolRuntime) -> str:
    """Retrieve the storred preferences"""
    try:
        preferences = runtime.state["preferences"]
    except KeyError:
        return "No preferences available yet"
    if not preferences:
        return "No preferences available yet"
    return f"User preferences are {preferences}"


tools_list = [Search_RAG, Search_Web, Store_Preferences, Get_Preferences]