"""
TP LangChain: Agent chef personnel

 -Receive message: la liste des ingrédients disponibles dans le réfrigérateur
 -Memory: mémoriser les préférences ou informations fournies par l’utilisateur
 -tools: utiliser un outil de recherche web pour compléter ses connaissances culinaires si nécessaire (recettes, techniques, associations d’ingrédients)
 -Proposing one or multiple dishes based on the provided ingredients

"""

import os
from dotenv import load_dotenv
from langchain.tools import tool
from typing import Dict, Any
from tavily import TavilyClient
from langchain_ollama import ChatOllama
from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver
from langchain.messages import HumanMessage


load_dotenv()

def websearch_tool_builder():
    #This function build the search too and gracefuly return an error if the API key is not valid
    tavily_api_key = os.getenv("TAVILY_API_KEY")

    if not tavily_api_key:
        @tool("websearch")
        def websearch(query:str) -> Dict[str, Any]:
            """
            Websearch is unavailable due to wrong or missing Tavily API Key
            Args:
                query: research request
            """
            return{
                "status":"Error",
                "message":("Search is not available."
                "make sure you are using a valid API key for Tavily"),
                "query": query
            }
        return websearch
    
    tavily_client = TavilyClient(tavily_api_key)

    @tool("websearch")
    def websearch(query:str) -> Dict[str, Any]:
        """
        Recherche web pour compléter ses connaissances culinaires si nécessaire 
        (recettes, techniques, associations d’ingrédients)

        Args:
            query: Question sur des recettes ou ingrédients
        """
        return tavily_client.search(query, max_results=5)
    return websearch


def buildAgent():
    #Create an agent
    model_name = os.getenv("MODEL_OLLAMA")

    llm = ChatOllama(model=model_name, temperature=0)

    system_prompt = """
            Tu es un chef cuisinier personnel intelligent.

            ========================
            RÔLE
            ========================
            Tu aides l'utilisateur à cuisiner avec les ingrédients disponibles.
            Tu proposes des recettes simples, rapides et adaptées à ses contraintes.
            Tu peux mémoriser ses préférences alimentaires, allergies et habitudes.

            ========================
            OUTIL DISPONIBLE (STRICT)
            ========================
            Il existe exactement UN SEUL outil :
            - web_search

            RÈGLES ABSOLUES SUR LES OUTILS :
            - Tu ne dois utiliser QUE l'outil "web_search".
            - Il est INTERDIT d'inventer, deviner ou créer d'autres outils ou fonctions.
            - Toute autre nom de fonction (ex: getRecipe, generateRecipe, proposeRecette) est invalide et interdit.
            - Tu ne dois jamais afficher ou simuler un appel d'outil.
            - Les appels d'outils sont gérés en interne par le système.

            UTILISATION DE web_search :
            - Utilise web_search uniquement si une information culinaire précise, technique ou récente est nécessaire.
            - Sinon, réponds directement sans utiliser d'outil.

            ========================
            RÈGLES DE RÉPONSE
            ========================
            - Réponds toujours en français.
            - N'utilise jamais JSON, code, ou format structuré.
            - N'utilise jamais de format de fonction ou de paramètres.
            - Ne décris jamais un raisonnement sous forme d'action technique.
            - N'invente jamais d'ingrédients qui ne sont pas fournis par l'utilisateur.
            - Si une information manque, fais une hypothèse raisonnable et indique-la.
            - Privilégie des recettes simples, rapides (≤ 20 minutes), et réalistes.
            - Sois clair, direct, et utile.

            ========================
            FORMAT OBLIGATOIRE
            ========================
            1.Plat proposé
            2.Pourquoi ce plat convient
            3.Ingrédients
            4.Étapes
            5.Variante ou conseil
        """

    agent = create_agent(model = llm,
                          tools=[websearch_tool_builder()],
                          system_prompt= system_prompt,
                          checkpointer= InMemorySaver())
    
    return agent


def askAgent(agent, userMessage : str, thread_id : str ="chef-1") -> str:
    #Asks the agent a question 
    response = agent.invoke(
        {"messages": [HumanMessage(content=userMessage)]},
        {"configurable": {"thread_id":thread_id}}
    )

    return response["messages"][-1].content


def run_demo():
    #Demonstration
    agent = buildAgent()

    user_prompt = """
        Bonjour Chef

        Voici les ingrédients que j’ai chez moi :
        - pâtes
        - tomates
        - farine
        - sel
        - fromage
        - blanc de poulet
        - viande hachée

        Contexte :
        - Nombre de personnes : 1
        - Temps disponible : 60 minutes
        - Préférence alimentaire : riche en protéines
        - Objectif : proposer une recettes

        Instructions :
            - Tu ne dois utiliser QUE les ingrédients listés ci-dessus.
            - Il est STRICTEMENT interdit d’inventer ou d’ajouter des ingrédients qui ne sont pas dans la liste.
            - Si une recette nécessite un ingrédient manquant, propose-le uniquement comme optionnel ou alternative clairement indiquée.
            - Si possible, privilégie des recettes qui n’ajoutent aucun ingrédient supplémentaire.
    """



    print("\n=================Question================")
    print(f"\n Utilisateur: {user_prompt}")
    answer = askAgent(agent=agent, userMessage= user_prompt)
    print(f"Agent: {answer}")

def interactive_demo():
    #Interractive agent

    agent = buildAgent()

    print("======================================================================")
    print("Agent chef personnel dans mode interactive.")
    print("Taper 'bye' pour quitter.\n")

    while True:
        user_prompt = input("Vous: ")
        if(user_prompt.lower() in {"bye", "quit", "exit"}):
            print("Fin de session")
            break
        if not user_prompt:
            continue

        answer = askAgent(agent=agent, userMessage=user_prompt)
        print("\n")
        print(f"Chef: {answer}\n")

if __name__ == "__main__":
    mode = os.getenv("MODE").lower()
    if(mode == "interactive"):
        interactive_demo()
    else:
        run_demo()