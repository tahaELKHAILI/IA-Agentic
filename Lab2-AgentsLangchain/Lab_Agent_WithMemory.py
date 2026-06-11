from langchain_ollama import ChatOllama
from langchain.agents import create_agent
from langchain.messages import HumanMessage
from langgraph.checkpoint.memory import InMemorySaver

import os
from dotenv import load_dotenv

load_dotenv()
model_name = os.getenv("MODEL_OLLAMA")
model = ChatOllama(model=model_name, temperature=0)

agent = create_agent(model=model, checkpointer=InMemorySaver())

question = HumanMessage(content="Bonjour, mon nom est Sami et je suis un développeur.")
config = {"configurable": {"thread_id": "1"}}

response = agent.invoke({"messages": [question]},config)

question = HumanMessage(content="Quel est mon métier ?")

response = agent.invoke({"messages": [question]},config)

print(response['messages'][-1].content)