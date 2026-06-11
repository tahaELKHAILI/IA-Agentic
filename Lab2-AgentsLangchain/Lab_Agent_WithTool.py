import os
from dotenv import load_dotenv

from langchain.agents import create_agent
from langchain.messages import HumanMessage
from langchain.tools import tool
from langchain_ollama import ChatOllama



@tool("meteo_capital")
def meteo_capital(ville:str) -> str:
    """
    Donne la météo d'une capitale (valeurs fixes pour test).
    Args:
    ville: nom de la capitale
    """
    print("tool meteo_capitale utilisé")
    temperature = 25
    humidity = 60
    pressure = 1013
    return(
        f"Météo à {ville} : "
        f"Température = {temperature}°C, "
        f"Humidité = {humidity}%, "
        f"Pression = {pressure} hPa"
    )

load_dotenv()

model_name = os.getenv("MODEL_OLLAMA")
model = ChatOllama(model=model_name, temperature=0)

system_prompt = "Utilises les tools pour répondre aux questions"
agent = create_agent(model=model, system_prompt=system_prompt, tools=[meteo_capital])

question = HumanMessage(content="Quelle est la météo à Capitole lunaire ?")

response = agent.invoke({"messages": [question]})

print(response['messages'][-1].content)
