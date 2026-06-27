# This scrip split the data into chunks

from pathlib import Path
import sys
sys.path.append(str(Path(__file__).resolve().parents[2]))


from config.config import CHUNK_OVERLAP, CHUNK_SIZE
from src.RAG.loader import RAG_Data
from langchain_text_splitters import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP, add_start_index=True
)

chunks = text_splitter.split_documents(RAG_Data)

