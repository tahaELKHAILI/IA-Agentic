# TP Agents using LangChain
This project contain practice elements from the class covering the creation of agents
## Contenu
* `Lab_Creating_Agent.py` Basic agent to answer questions
* `Lab_Agent_WithTool.py` Agent using a tool
* `Lab_Agent_WebSearchTool.py` Agent using a web search tool through API Tavily
* `Lab_Agent_WithMemory.py` Agent with memory
* `TP_Agent_Personal_Chef.py` Project using all the elemts taught in previous labs 
        (memory, web search tool)

## Environnement file
        MODEL_OLLAMA = llama3.2:latest
        TAVILY_API_KEY  = --Insert your API Key--
        MODE = Interactive --Remove this for a direct execution for the preset user message
## UV setup
        uv venv -- to create your project's virtual environnement
        uv sync -- synchronizes your project’s virtual environment with your exact dependency specifications
## Dependencies
        python = >=3.14
        langchain>=1.3.7
        langchain-community>=0.4.2
        langchain-ollama>=1.1.0
        tavily>=1.1.0
## Execution
        python *Insert script name*.py
        Example. python Lab_Agent_WithMemory.py
## Screenshots
### Executing a non interactive version
Automatic prompts:
![alt text](screenshots/PromptAutomatique.png)

Agent reply:
![alt text](screenshots/AutoPromptAgentReply.png)

### Executing interactive version
![alt text](screenshots/ModeInteractive.png)

## Notes
* The scripts require an active ollama server with a local model.
* For`Lab_Agent_WebSearchTool.py` you need valid API keys for Tavily