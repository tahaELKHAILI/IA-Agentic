import os
from dotenv import load_dotenv

from langchain.agents import create_agent
from langchain.messages import HumanMessage
from langchain_ollama import ChatOllama
from pydantic import BaseModel

load_dotenv()

model_name = os.getenv("MODEL_OLLAMA")

#Création d’un nouveau agent sans System Message

model = ChatOllama(model=model_name, temperature=0)

agent = create_agent(model = model)

question = HumanMessage("Quelle est la capital de la lune ?")

response = agent.invoke({"messages":[question]})

print("================Model 1 response====================")
print(response['messages'][-1].content)

#Agent avec System Message : un message de contrôle qui définit le comportement global du modèle

system_prompt = "Vous êtes un auteur de science-fiction ; créez une capitale à la demande des utilisateurs."

scifi_agent = create_agent(model = model, system_prompt=system_prompt)

response = scifi_agent.invoke({"message": [question]})

print("================Model 2 response====================")
print(response['messages'][-1].content)

#Agent avec Few-shot learning : une méthode où le modèle apprend une nouvelle tâche ou classe à partir de quelques exemples seulement

system_prompt = """
Vous êtes un auteur de science-fiction et vous devez créer une capitale spatiale à la demande d'un utilisateur.
Utilisateur : Quelle est la capitale de Mars ?
Auteur : Marsialis
Utilisateur : Quelle est la capitale de Vénus ?
Auteur : Venusovia
"""

scifi_agent = create_agent(model=model,system_prompt=system_prompt)

response = scifi_agent.invoke({"messages": [question]})

print("================Model 3 response====================")
print(response['messages'][-1].content)

#Agent avec réponse structurée: une sortie organisée selon un format prédéfini, plutôt que du texte libre.

system_prompt = """
Vous êtes un auteur de science-fiction et vous devez créer une capitale spatiale à la demande d'un utilisateur.
Veuillez respecter la structure ci-dessous.
Nom : Nom de la capitale
Localisation : Lieu où elle est située
Ambiance : Description en 2 ou 3 mots
Économie : Principaux secteurs d'activité
"""

scifi_agent = create_agent(model=model,system_prompt=system_prompt)

response = scifi_agent.invoke({"messages": [question]})

print("================Model 4 response====================")
print(response['messages'][-1].content)

#Agent avec réponse structurée en utilisant BaseModel : rendre la réponse facile à exploiter automatiquement par un programme ou un système.

class CapitalInfo(BaseModel):
    nom: str
    Localisation: str
    Ambiance: str
    Économie: str

system_prompt = """
Vous êtes un auteur de science-fiction et vous devez créer une capitale spatiale à la demande d'un utilisateur.
Veuillez respecter la structure ci-dessous.
Nom : Nom de la capitale
Localisation : Lieu où elle est située
Ambiance : Description en 2 ou 3 mots
Économie : Principaux secteurs d'activité
"""

agent = create_agent(model=model, system_prompt=system_prompt, response_format=CapitalInfo)

response = agent.invoke({"messages": [question]})

print("================Model 5 response====================")
print(response["structured_response"])

