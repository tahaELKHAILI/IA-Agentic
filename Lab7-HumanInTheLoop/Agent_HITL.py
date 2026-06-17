import os
from dotenv import load_dotenv

from langchain.tools import tool, ToolRuntime
from langchain.agents import create_agent, AgentState
from langgraph.checkpoint.memory import InMemorySaver
from langchain.agents.middleware import HumanInTheLoopMiddleware
from langchain_ollama import ChatOllama
from langchain.messages import HumanMessage
from langgraph.types import Command

@tool
def read_email(runtime:ToolRuntime)->str:
    """Read an email from a given address."""
    return runtime.state["email"]

@tool
def send_email(body:str) ->str:
    """Send an email to the given address with the given subject and body."""
    #place
    return f"Email sent"


# Creating agent Human in the loop

# Agent creation
class EmailState:
    email:str

load_dotenv()

model_name = os.getenv("MODEL_OLLAMA")
llm = ChatOllama(model=model_name, temperature=0)

agent = create_agent(model=llm,
                     tools=[send_email, read_email],
                     checkpointer=InMemorySaver(),
                     state_schema=EmailState,
                     middleware=[HumanInTheLoopMiddleware(
                         interrupt_on={
                             "read_email": False,
                             "send_email": True
                         },
                         description_prefix="Tool execution requires approval"
                     )])

# Testing agent
config = {"configurable": {"thread_id": "1"}}

response = agent.invoke(
        {
        "messages": [HumanMessage(content="Veuillez lire mon e-mail et envoyer une réponse immédiatement."
        "Envoyez la réponse maintenant dans le même fil de discussion.")],
        "email": "Bonjour Sara, je vais être en retard pour notre réunion de demain. Pouvons-nous la"
        "reprogrammer ? Cordialement, Sofia"
        },
config=config
)
print("=====Part 2===============")
#print(response)   # this one show the whole response
#print(response['__interrupt__']) # this one show the interrupted response
print(response['__interrupt__'][0].value['action_requests'][0]['args']['body'])  # this one show the suggested message

# Part 3 approving the message
response = agent.invoke(
    Command(
        resume={"decisions": [{"type": "approve"}]}

    ),
    config=config # Le même thread ID pour reprendre la conversation
    )

print("=====Part 3===============")
print(response['messages'][-1].content)

# Part 4 - refusing the result
response = agent.invoke(
Command(
    resume={
        "decisions": [
            {
            "type": "reject",
            # Une explication sur les raisons du rejet
            "message": " J’annule notre rendez-vous."
            }
        ]
        }
    ),
    config=config # Le même thread ID pour reprendre la conversation
)
print("=====Part 4===============")
print(response)

# Part 5 - modifying the result
response = agent.invoke(
    Command(
        resume={
            "decisions": [
                {
                    "type": "edit",
                    "edited_action": {
                    # Le nom du Tool.
                    "name": "send_email",
                    # Les arguments à passer au tool.
                    "args": {"body": "Je suis désolée mais je dois annuler notre rendez-vous je ne serais pas libre."
                    "taha"},
                    }
                }
                ]
            }
        ),
config=config # Le même thread ID pour reprendre la conversation
)

print("=====Part 5===============")
print(response['messages'][-1].content)