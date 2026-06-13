from langchain_community.utilities import SQLDatabase
from langchain_ollama import ChatOllama
from langchain.tools import tool
from langchain.messages import HumanMessage
from langchain.agents import create_agent

import os
from dotenv import load_dotenv


#Connexion à une base de données SQL (SQLite) avec LangChain
db = SQLDatabase.from_uri("sqlite:///resources/Chinook.db")

#Création d’un tool personnalisé pour interroger une base SQL avec un agent

@tool("sql_query")
def sql_query(query:str)-> str:
    """
    Obtain information from the database using SQL queries
    args:
        query
    """
    try:
        print(f"Executing query: {query}")
        return db.run(query)
    except Exception as e:
        return f"Error: {e}"

sql_query.invoke("SELECT * FROM Artist LIMIT 10")

#Création d’un agent LLM pour interroger une base SQL

load_dotenv()
model_name = os.getenv("MODEL_OLLAMA")

llm = ChatOllama(model=model_name, temperature=0)

system_prompt = """You are a SQL expert.
Rules:
- Only use sql_query tool
- The sql_query tool takes a SQL query as input and returns the result of the
query.
- Only use available columns
- If information does not exist, say so
- Do not guess
- you have to return the results in a human readable format, do not return raw
SQL results or a sql query.
Database schema:
Table Artist:
- ArtistId
- Name
"""

agent = create_agent(model=llm,
                     tools=[sql_query],
                     system_prompt=system_prompt)

#Interrogation d’un agent SQL via langage naturel et récupération des résultats
user_prompt = [HumanMessage(content="Give me the first 5 artists in the database")]

response = agent.invoke({
    "messages":user_prompt
})

print(response['messages'][-1].content)