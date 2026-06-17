from langgraph.graph import StateGraph, MessagesState, START, END

def hellor_node(state:MessagesState):
    #returns a message state
    return {"messages": [{"role":"ai",
             "content":"Hello world"}]}

builder = StateGraph(MessagesState)
builder.add_node("hello", hellor_node)
builder.add_edge(START, "hello")
builder.add_edge("hello", END)

graph = builder.compile()

response = graph.invoke({"messages": [{"role": "user", "content": "Hi"}]})

print(response["messages"][-1].content)