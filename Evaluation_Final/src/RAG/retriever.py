# This script generates the retriever

from src.RAG.vectorStore import vector_store

retriever = vector_store.as_retriever()

print("RAG set properly")