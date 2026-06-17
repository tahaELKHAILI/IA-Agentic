import os
from dotenv import load_dotenv

from langchain.tools import tool
from langchain_ollama import ChatOllama
from langchain.agents import create_agent
from langchain.messages import HumanMessage

load_dotenv()


@tool
def rag_search_opt(query:str) -> str:
    """ Recherche des informations dans le text"""
    results = (
        "Le personnage principale est un jeune homme nommé Jack, "
        "qui découvre un ancien artefact magique. "
        "Cet artefact lui confère des pouvoirs extraordinaires mais attire également "
        "des ennemis redoutables. Jack devra apprendre à maîtriser ses nouveaux pouvoirs "
        "tout en protégeant ses proches."
    )
    return results
model_name = os.getenv("MODEL_OLLAMA")
llm= ChatOllama(model=model_name, temperature=0)

agent = create_agent(
    model=llm,
    tools=[rag_search_opt],
    system_prompt=(
    "Tu es un assistant spécialisé dans l'analyse de texte. "
    "Utilise l'outil rag_search_opt pour répondre aux questions en te basant sur le texte. "
    "Réponds de manière précise et cite les informations du contexte."
    )
)
