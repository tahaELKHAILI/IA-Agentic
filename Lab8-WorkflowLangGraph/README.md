# LAB 8 - Workflow using LangChain
## Objectif
Discover the basic building blocks of a LangGraph workflow: state graph, nodes, edges, reducers, message-type state, conditional branches and loops.
## Files overview
    Lab8-WorkflowLangGraph
    |__01_Hello_World.py            -- Use of StateGraph and MessagesState
    |__02_TwoStep_Workflow.py       -- Two step workflow (Sequencial)
    |__03_Reducer_Trial.py       -- Reducer
    |__04_MessageState_Graph.py       -- Type message state
    |__05_ConditionalWorkflow.py       -- Conditional edges
    |__06_WorflowLoop.py       -- Loop workflow + generating graph as a png
## Requirements
    python = >=3.12
    ipython>=9.14.1
    langchain>=1.3.9
    langchain-ollama>=1.1.0
    langgraph>=1.2.5
## Starting the scripts
    uv run --active insert-file-name.py
    eg. uv run --active 01_Hello_World.py
