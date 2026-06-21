import os
from dotenv import load_dotenv
from pathlib import Path

from langchain_ollama import ChatOllama
from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver

from src.Tools_Setup import ChefState, tools_list

project_root = Path(__file__).resolve().parent.parent
load_dotenv(project_root / ".env")

model_name = os.getenv("MODEL_OLLAMA")

llm = ChatOllama(model=model_name, temperature=0)

system_prompt = """You are a personal chef assistant. Your role is to help users discover
delicious dishes they can prepare with the available ingredients.

You have access to:
- search_rag: search your local recipe knowledge base
- search_web: search the internet for additional recipes and techniques
- store_preference: store user preferences, allergies, and dietary restrictions
- get_preferences: retrieve the user's stored preferences

When a user tells you their available ingredients:
1. First check their preferences with get_preferences
2. Search the recipe knowledge base with Search_RAG
3. Suggest 3 concrete, detailed dishes adapted to their ingredients and preferences
4. Always respect their dietary restrictions and allergies

When a user shares a preference, allergy, or dietary restriction, save it with store_preference.

Be enthusiastic, helpful, and creative like a professional chef!

and make sure to specify if the receip comes from the itnernal database or the web

Only use the tools I provided to you. 
"""


AgentChef = create_agent(model=llm,
                         tools=tools_list,
                         checkpointer=InMemorySaver(),
                         state_schema= ChefState,
                         system_prompt=system_prompt)

