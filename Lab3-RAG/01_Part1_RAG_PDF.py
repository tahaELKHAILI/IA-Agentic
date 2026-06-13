from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore

from langchain.agents import create_agent
from langchain.messages import HumanMessage
from langchain_ollama import ChatOllama
from langchain.tools import tool

import os
from dotenv import load_dotenv

#Chargement et extraction de pdf
file = "resources/acmecorp-employee-handbook.pdf"
loader =PyPDFLoader(file)
data = loader.load()
print(data)

#Segmentation de texte pour préparation au RAG avec LangChain
text_spliter = RecursiveCharacterTextSplitter(
    chunk_size = 1000, 
    chunk_overlap = 200,
    add_start_index = True)
all_splits = text_spliter.split_documents(data)
print(len(all_splits))

#Transformation des chunks en vecteurs sémantiques avec un modèle Hugging Face : Génération d’embeddings textuels
embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
)

#Création d’une base vectorielle en mémoire pour stockage et recherche d’embeddings
vector_store = InMemoryVectorStore(embedding=embeddings)

#Indexation des documents dans la base vectorielle pour recherche sémantique
ids = vector_store.add_documents(documents=all_splits)

#Recherche sémantique dans une base vectorielle pour retrouver les informations pertinentes
results = vector_store.similarity_search(
    "How many days of vacation does an employee get in their first year?"
)
print(results[0])

#Agent RAG

#Tool to search the handbook

@tool("search_handbook")
def search_handbook(query:str) -> str:
    """
    Search the handbook for relevent information.
    args:
        query
    """
    results = vector_store.similarity_search(query)
    return results[0].page_content

load_dotenv()
model_name = os.getenv("MODEL_OLLAMA")

llm = ChatOllama(model=model_name,
                 temperature=0)

system_prompt="You are a helpful agent that can search the employee hand-book for information."

agent = create_agent(model=llm,
                     tools=[search_handbook],
                     system_prompt=system_prompt)

human_message = [HumanMessage(content="How many days of vacation does an employee get in their first year?")]

response = agent.invoke({
    "messages":human_message
})

print(response['messages'][-1].content)