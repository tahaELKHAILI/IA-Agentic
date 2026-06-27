from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[2]))

from langchain_core.vectorstores import InMemoryVectorStore
from langchain_chroma import Chroma

from config.config import VECTOR_STORE, VECTOR_DB_DIR
from src.RAG.embeddings import embeddings
from src.RAG.splitter import chunks


if VECTOR_STORE == "memory":
    print("Using InMemoryVectorStore...")

    vector_store = InMemoryVectorStore(embeddings)
    vector_store.add_documents(chunks)

elif VECTOR_STORE == "chroma":
    print("Using Chroma...")

    vector_store = Chroma(
        persist_directory=str(VECTOR_DB_DIR),
        embedding_function=embeddings,
    )

    # Only build the database if it's empty
    if vector_store._collection.count() == 0:
        print("Creating vector database...")
        vector_store.add_documents(chunks)
        print("Vector database created.")

    else:
        print("Loaded existing vector database.")

else:
    raise ValueError(f"Unknown vector store: {VECTOR_STORE}")