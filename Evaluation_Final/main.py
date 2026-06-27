from langchain_core.messages import HumanMessage
from src.graph.graph import graph

if __name__ == "__main__":

    config = {
        "configurable": {
            "thread_id": "session-1"
        }
    }

    print("\nChat with your RAG agent (type 'exit' to quit)\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit"]:
            break

        result = graph.invoke(
            {
                "messages": [
                    HumanMessage(content=user_input)
                ]
            },
            config=config
        )

        print("\nAgent:", result["messages"][-1].content)
        print("\n" + "-" * 50 + "\n")