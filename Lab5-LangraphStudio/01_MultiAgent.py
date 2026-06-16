import os
from dotenv import load_dotenv


from langchain.tools import tool
from langchain_ollama import ChatOllama
from langchain.agents import create_agent
from langchain.messages import HumanMessage



# Part 1 Defining two tools

@tool
def squar_root(x:float) -> float:
    """ calculate the square root of a number """
    return x**0.5

@tool
def squar(x:float) -> float:
    """ calculate the square of a number"""
    return x**2


# Part 2 Submodels
load_dotenv()
model_name = os.getenv("MODEL_OLLAMA")
model = ChatOllama(model = model_name, temperature=0)

subagent1 = create_agent(model=model,
                         tools=[squar_root])

subagent2 = create_agent(model=model,
                         tools=[squar])

# Part 3 Main agent

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


main_agent = create_agent(model = model,
                          tools=[call_subagent_1, call_subagent_2],
                          system_prompt="You are a helpful assistant who can call subagents to calculate the square root or the square of a number.")


# Part 4 Calling the agent
question = "What is the square root of 456? give me the number"
response = main_agent.invoke({"messages": [HumanMessage(content=question)]})
print(response['messages'][-1].content)


question = "What is the square 12? give me the number"
response = main_agent.invoke({"messages": [HumanMessage(content=question)]})
print(response['messages'][-1].content)