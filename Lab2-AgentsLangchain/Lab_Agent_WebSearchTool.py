import os
from dotenv import load_dotenv

from typing import Dict, Any
from tavily import TavilyClient
from langchain.tools import tool
from langchain_ollama import ChatOllama
from langchain.agents import create_agent
from langchain.messages import HumanMessage

from dotenv import load_dotenv


load_dotenv()
model_name = os.getenv("MODEL_OLLAMA")

tavily_client = TavilyClient()

@tool("web_search")
def web_search(query: str) -> Dict[str, Any]:
    """ effectuer une recherche sur le web en utilisant l'API de Tavily. Args: querry: la requete de recherche """
    return tavily_client.search(query)

web_search.invoke("Qui est le Président de commune actuel de Marrakech ?")

model = ChatOllama(model= model_name, temperature=0)
agent = create_agent(model = model, tools=[web_search])

question = HumanMessage(content="Qui est le Président de commune actuel de Marrakech ?")

response = agent.invoke({"messages": [question]})

print(response['messages'][-1].content)