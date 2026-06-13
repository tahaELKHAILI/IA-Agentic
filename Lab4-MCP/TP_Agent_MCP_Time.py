import asyncio
from langchain.agents import create_agent
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
from langchain.messages import HumanMessage
from langchain_ollama import ChatOllama

import os
from dotenv import load_dotenv


async def main():
    client = MultiServerMCPClient(
        {
            "time": {
            "transport": "stdio",
            "command": "uvx",
            "args": [
            "mcp-server-time",
            "--local-timezone=America/New_York"
                ]
            }
        }
    )

    #Récupération dynamique des tools
    tools = await client.get_tools()

    # Initialiser le modèle Ollama
    load_dotenv()

    model = ChatOllama(
    model=os.getenv("MODEL_OLLAMA"), # ou mistral, gemma, etc.
    )
    agent = create_agent(
    model=model,
    tools=tools,
    )
    question = HumanMessage(content="What time is it in Japan")
    response = await agent.ainvoke(
    {"messages": [question]}
    )

    print(response['messages'][-1].content)

asyncio.run(main())