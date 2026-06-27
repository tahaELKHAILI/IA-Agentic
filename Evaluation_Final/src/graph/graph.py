#Generating the graph

from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import InMemorySaver
from src.graph.state import State
from src.graph.nodes import llm_node, tool_node, should_continue


builder = StateGraph(State)

# Nodes
builder.add_node("llm", llm_node)
builder.add_node("tool", tool_node)


# Start
builder.add_edge(START, "llm")


# Conditional edge
builder.add_conditional_edges(
    "llm",
    should_continue,
    {
        "tool": "tool",
        "end": END
    }
)


# Loop back to tool
builder.add_edge("tool", "llm")


# Build graph
graph = builder.compile(checkpointer=InMemorySaver())