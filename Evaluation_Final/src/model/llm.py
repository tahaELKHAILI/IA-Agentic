# This script generates the model

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from langchain_ollama import ChatOllama
from config.config import MODEL_OLLAMA, TEMPERATURE
from src.tools.tools import TOOLS

llm = ChatOllama(model=MODEL_OLLAMA, 
                 temperature= TEMPERATURE
                 )

llm_with_tools = llm.bind_tools(TOOLS)