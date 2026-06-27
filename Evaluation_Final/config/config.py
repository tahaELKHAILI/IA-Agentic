# This file contain the constants needed in the project

from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR /"resources"
VECTOR_DB_DIR = BASE_DIR / "chroma_db"

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 500

MODEL_OLLAMA = "llama3.2:latest"
TEMPERATURE = 0

EMBEDDING_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"


#  Remove the # from the option you want to use and add it to the option you are not using
#  This variable controls if you want to use persistance or not
# VECTOR_STORE = "memory"
VECTOR_STORE = "chroma"