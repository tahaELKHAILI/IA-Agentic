import os
from dotenv import load_dotenv

from langchain.tools import tool
from langchain_ollama import ChatOllama

load_dotenv()

# PART 1: Local LLM with tools
# Creating Tools
@tool
def add(a:int, b:int) -> int:
    """Add two integers."""
    return a+b

@tool
def multiply(a:int, b:int)->int:
    """Multiply two integers."""
    return a*b

@tool
def divide(a:int, b:int)->int:
    """Divide two integers."""
    return a/b

# Creating the model

model_name = os.getenv("MODEL_OLLAMA")
model = ChatOllama(model=model_name, temperature=0)

tools = [add, multiply, divide]

tools_by_name = {t.name: t for t in tools}

model_with_tools = model.bind_tools(tools)