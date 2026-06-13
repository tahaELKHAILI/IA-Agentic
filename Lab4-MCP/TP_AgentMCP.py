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
                "local_server": {
                "transport": "stdio",
                "command": "python",
                "args": ["mcp_local_server.py"],
                }
            }
        )
    
    #Récupération dynamique des tools
    tools = await client.get_tools()
    #Resources MCP
    resources = await client.get_resources("local_server")
    #Prompt dynamique côté serveur MCP
    prompt = await client.get_prompt("local_server", "prompt")
    prompt = prompt[0].content

    # Initialiser le modèle Ollama
    load_dotenv()
    
    model = ChatOllama(
        model=os.getenv("MODEL_OLLAMA"),
        temperature=0
    )

    agent = create_agent(
        model=model,
        tools=tools,
        system_prompt=prompt
    )

    config = {"configurable": {"thread_id": "1"}}

    response = await agent.ainvoke(
        {"messages": [HumanMessage(content="Tell me about the langchain-mcp-adapters library")]},
        config=config
    )

    print(response)

asyncio.run(main())