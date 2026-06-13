# TP Model Context Protocol (MCP)
Integrate the Model Context Protocol (MCP) with LangChain to connect LLM agents to local and remote MCP servers via different transports (stdio, HTTP streaming).
## Contenu
* `MCP_Local_Server.py` Local MCP server (stdio) — tools + resources + prompts
* `TP_Agent_MCP_Time.py` Agent with MCP time server
* `TP_AgentMCP.py` Agent with local MCP server
* `TP_Agent_MCP_HTTP.py` Agent calling a distant server
## Environnement file
        MODEL_OLLAMA = llama3.2:latest
        TAVILY_API_KEY  = --Insert your API key
        OPENAI_API_KEY =  --Insert your API key
        
## UV setup
        uv venv -- to create your project's virtual environnement
        uv sync -- synchronizes your project’s virtual environment with your exact dependency specifications
## Dependencies
        python = >=3.14
        langchain>=1.3.9
        langchain-community>=0.4.2
        langchain-mcp-adapters>=0.3.0
        langchain-ollama>=1.1.0
        langchain-openai>=1.3.2
        mcp>=1.27.2
        tavily>=1.1.0
## Execution
        uv --active python *Insert script name*.py
        Example. python Lab_Agent_WithMemory.py
## Notes
* The scripts require an active ollama server with a local model
* Tavily API key is needed to run `MCP_Local_Server.py` 
* `TP_Agent_MCP_HTTP.py` require a valid openAI API key
