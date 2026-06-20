# LAB 9 - Agent using LangGraph
## Objectif
Gradually build a complete LangGraph agent: an LLM with tools, run as a graph node, capable of stopping for human validation (HITL), resuming after interruption, keeping its checkpoint history and "forking" (going back to the past and restarting from a modified state).
## Files overview
    Lab9-AgentLangGraph
    |__ tools_setup.py        # Part 1 : Local LLM + tools (arithmetics)
    |__ agent_node.py         # Part 2 : Agent as graph nodes (llm_call / llm_tools)
    |__ HITL_workflow.py      # Part 3 : @entrypoint/@task workflow with interrupt() (HITL)
    |__ tp_Agent.py  # Part 4 : Agent using tools HITL history and fork

## Requirements
    requires-python = >=3.12
    dotenv>=0.9.9
    langchain>=1.3.10
    langchain-ollama>=1.1.0

## Starting the scripts
    uv run --active insert-file-name.py
    eg. uv run --active tp_advanced_agent.py

## Note
* An active OLLAMA server is needed
