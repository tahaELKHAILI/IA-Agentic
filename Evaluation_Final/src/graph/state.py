# This script manages the state

from typing import TypedDict, Optional, List, Annotated
from langchain_core.documents import Document
from langchain_core.messages import AnyMessage
from langgraph.graph.message import add_messages

class State(TypedDict):
    question: str
    context: Optional[str]
    answer: Optional[str]
    documents: Optional[List[Document]]
    messages: Annotated[list[AnyMessage], add_messages]