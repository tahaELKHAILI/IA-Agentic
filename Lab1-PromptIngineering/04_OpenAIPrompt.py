from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv(override=True)

model = "gpt-5.2"

llm = ChatOpenAI(model=model)

response = llm.invoke([
    {"role":"system", "content":"You are a helpful assistant. The output should be in Markdown"},
    {"role":"user","content":"C'est quoi un Agent AI"}
])

print(response.content)