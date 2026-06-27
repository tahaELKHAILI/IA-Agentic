# This script manages the nodes

from langchain_core.messages import SystemMessage
from langchain_core.messages import ToolMessage
from src.tools.tools import TOOL_MAP
from src.model.llm import llm_with_tools
from src.model.systemPrompt import SYSTEM_PROMPT

def llm_node(state):
    messages = state["messages"]

    response = llm_with_tools.invoke(
        [SystemMessage(content=SYSTEM_PROMPT)] + messages
    )

    return {"messages": [response]}


def tool_node(state):
    messages = []

    if not state["messages"]:
        return {"messages": []}

    last_message = state["messages"][-1]
    tool_calls = getattr(last_message, "tool_calls", None)

    if not tool_calls:
        return {"messages": []}

    for call in tool_calls:
        tool = TOOL_MAP.get(call["name"])

        if tool is None:
            observation = f"Unknown tool: {call['name']}"
        else:
            try:
                observation = tool.invoke(call["args"])
            except Exception as e:
                observation = f"Tool error ({call['name']}): {str(e)}"

        messages.append(
            ToolMessage(
                content=str(observation),
                tool_call_id=call["id"]
            )
        )

    return {"messages": messages}


def should_continue(state) -> str:
    if not state["messages"]:
        return "end"

    last_message = state["messages"][-1]
    tool_calls = getattr(last_message, "tool_calls", None)

    if tool_calls:
        return "tool"

    return "end"