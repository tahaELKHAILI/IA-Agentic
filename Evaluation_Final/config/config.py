import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR /"resources"


CHUNK_SIZE = 1000
CHUNK_OVERLAP = 500

MODEL_OLLAMA = "llama3.2:latest"
TEMPERATURE = 0

EMBEDDING_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"