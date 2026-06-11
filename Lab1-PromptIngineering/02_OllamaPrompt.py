import os
from dotenv import load_dotenv
from langchain_ollama import ChatOllama

load_dotenv()

model = os.getenv("MODEL_OLLAMA")

llm = ChatOllama(model=model)

response = llm.invoke([
    {"role": "system", "content": "You are a helpful assistant. The output should be in markdown"},
    {"role": "user", "content": "C'est quoi un agent AI"}
])

print(response.content)