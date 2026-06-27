# This scirpt create the vector of data for the RAG

from langchain_core.vectorstores import InMemoryVectorStore
from src.RAG.embeddings import embeddings
from src.RAG.splitter import chunks

vector_store = InMemoryVectorStore(embeddings)

ids = vector_store.add_documents(documents=chunks)