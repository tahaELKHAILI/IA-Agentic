# This script is for the embedding model
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).resolve().parents[2]))

from langchain_huggingface import HuggingFaceEmbeddings
from config.config import EMBEDDING_MODEL_NAME



embeddings = HuggingFaceEmbeddings(model_name = EMBEDDING_MODEL_NAME)



