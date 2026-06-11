from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.messages import SystemMessage, HumanMessage

load_dotenv(override=True)

model = "openai/gpt-oss-120b"
llm = ChatGroq(model = model)

response = llm.invoke([
    SystemMessage("You are a helpful assistant. The output should be in markdown"),
    HumanMessage("C'est quoi un agent AI")
])

print(response.content)