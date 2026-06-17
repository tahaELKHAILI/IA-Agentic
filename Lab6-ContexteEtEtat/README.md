# LAB 6 - Context and State
## Objectif
Purpose of this lad is to understand and put into practice the difference between context (immutable data provided at invocation) and state (mutable data that evolves and persists during the conversation) in a LangChain/LangGraph agent.
## Files
* `01_AgentContext.py` This agent uses a context 
* `02_AgentState.py` This agent uses a state
* `.env` contains `MODEL_OLLAMA = llama3.2:latest`
## UV setup
    uv venv -- to create your project's virtual environnement
    uv sync -- synchronizes your project’s virtual environment with your exact dependency specifications
## Statve vs Context
|Feature     |State       |Context      |
|------------|-------------|-------------|
|**Primary role** | Tracks task progress, session data, and memory history.| Provides the active "working memory" and instructions for an LLM to generate a response.|
|**Lifespan**| Long-term; can be stored persistently across user sessions in databases or memory stores. | Short-term; dynamically assembled, filtered, and passed into the model's context window per loop iteration.|
|**Composition** |Variables like tool execution status, active goals, intermediate results, and session IDs. | A compilation of system instructions, retrieved facts, task history, and recent tool outputs.|
|**handling** | Read and updated by the agent's orchestration engine. | Handled by context engineering (offloading, retrieval, and reduction) to keep the LLM within its token limits.|
## Dependencies
    requires-python = >=3.12
    langchain>=1.3.9
    langchain-community>=0.4.2
    langchain-ollama>=1.1.0
## Execution
    uv --active python *Insert script name*.py
    Example. uv --active python 01_AgentContext.py
## Note
* An active Ollama server is required
* No API keys are needed