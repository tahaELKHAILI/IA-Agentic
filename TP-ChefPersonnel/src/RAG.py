#===================================================#
# This file contains the set up for the RAG system  #
# File reading                                      #
# Segmentation                                      #
# Vectorisation                                     #
#===================================================#

from pathlib import Path
from dotenv import load_dotenv

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_huggingface import HuggingFaceEmbeddings

project_root = Path(__file__).resolve().parent.parent
load_dotenv(project_root / ".env")

# Load file
BASE_DIR = Path(__file__).resolve().parent.parent
file_path = BASE_DIR / "resources" / "receipes.txt"

receipe_text = file_path.read_text(encoding="utf-8")

# Splitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=200, chunk_overlap=10
)

chunks = text_splitter.split_text(receipe_text)


# Embedding
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2")

# Storing the embeddings in a db
vector_store = InMemoryVectorStore(embeddings)

# Indexing for search
ids = vector_store.add_texts(texts=chunks)
