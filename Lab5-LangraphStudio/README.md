# LAB 5 : LangGraph Studio & Multi-Agents
## Objectif
This folder contains two complementary practical exercises based on LangGraph Studio:
1. Visualizing, testing, and debugging an agent with LangGraph Studio — visualizing an agent's graph, executing it step by step, and inspecting the inputs/outputs of each node;
2. Building a hierarchical multi-agent system — a main agent that delegates subtasks to specialized sub-agents, exposed as simple tools, and observing everything in Studio.
## Requirment
* python = >=3.14
* langchain>=1.3.9
* langchain-community>=0.4.2
* langchain-ollama>=1.1.0
## .env file structure
MODEL_OLLAMA = llama3.2:latest

# TP: Multiagent using LangChain
## Architecture
    Main Agent [Call sub agent 1 or Call sub agent 2]
    |__Call_subagent_1
    |   |__subagent_1 [tool = square root]
    |__Call_subagent_2
        |__subagent_2 [tool = square]
        
All sub agents were created using `LangChain` 

`Main agent` has the ability to *call sub agent 1* or *sub agent 2* depending on the request from the user.

## Part 1: Tool definition
    @tool
    def squar_root(x:float) -> float:
        """ calculate the square root of a number """
        return x**0.5

    @tool
    def squar(x:float) -> float:
        """ calculate the square of a number"""
        return x**2
## Part 2: Subagents creation
    load_dotenv()
    model_name = os.getenv("MODEL_OLLAMA")
    model = ChatOllama(model = model_name, temperature=0)

    subagent1 = create_agent(model=model,
                            tools=[squar_root])

    subagent2 = create_agent(model=model,
                            tools=[squar])
## Part 3: Creating the main agent
### Main agent implementation
    main_agent = create_agent(model = model,
                            tools=[call_subagent_1, call_subagent_2],
                            system_prompt="You are a helpful assistant who can call subagents to 
                            calculate the square root or the square of a number.")
### Sub agents as tools
    @tool
    def call_subagent_1(x: float) -> float:
        """Call subagent 1 in order to calculate the square root of a number"""
        response = subagent1.invoke({"messages": [HumanMessage(content=f"Calculate the square root of {x}")]})
        return response["messages"][-1].content

    @tool
    def call_subagent_2(x: float) -> float:
        """Call subagent 2 in order to calculate the square of a number"""
        response = subagent2.invoke({"messages": [HumanMessage(content=f"Calculate the square of {x}")]})

        return response["messages"][-1].content
## Part 4: Running the agent
    uv run --active python 01_Multiagent.py
## Results
    I called a subagent to calculate the square root of 456, and they responded with the result: √456 ≈ 21.3542.
    I called a subagent to calculate the square of 12, and they responded with the result: 144.0.
**NOTE:** I had to add `give me the number` to my question as the model didn't print the result they received.
It just confirmed receiving an answer.