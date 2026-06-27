# This scrip contain all the tools for our model

from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1]))

from langchain.tools import tool
from src.RAG.retriever import retriever

# Tool 1: Get data from the files
@tool("retrieve")
def retrieve(query: str) -> str:
    """
    Search sustainability documents and return relevant context with sources.
    """

    results = retriever.invoke(query)

    if not results:
        return "No relevant documents found."

    context = "\n\n".join(
        f"[Source: {doc.metadata.get('source', 'unknown')}, "
        f"Page: {doc.metadata.get('page', 'N/A')}]\n"
        f"{doc.page_content}"
        for doc in results[:4]
    )

    return context        


# This tool explain specific concepts based on the provided documetation
@tool("explain_concept")
def explain_concept(query: str) -> str:
    """
    Explain sustainability concepts clearly using retrieved documentation.
    """

    results = retriever.invoke(query)

    if not results:
        return "No relevant information found."

    explanation = "\n\n".join(
        f"[Source: {doc.metadata.get('source', 'unknown')}, "
        f"Page: {doc.metadata.get('page', 'N/A')}]\n"
        f"{doc.page_content}"
        for doc in results[:3]
    )

    return explanation


TOOLS = [retrieve, explain_concept]
TOOL_MAP = {t.name: t for t in TOOLS}