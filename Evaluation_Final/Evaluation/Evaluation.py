from langchain_core.messages import HumanMessage
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.graph.graph import graph

questions = [
    # Simple questions
    "What is ESG?",
    "What are Scope 1 emissions?",
    "What are Scope 2 emissions?",
    "What are Scope 3 emissions?",
    "What is carbon accounting?",
    "What is sustainability reporting?",
    "What does GHG stand for?",
    "What is the purpose of ESG frameworks?",
    "What is GRI in sustainability reporting?",
    "Why do companies use GRI standards?",

    # Hard questions
    "What is the difference between ESG reporting and GRI standards?",
    "How does GRI help companies structure sustainability reports?",
    "Compare Scope 1, Scope 2, and Scope 3 emissions in GRI reporting.",
    "Why is GRI widely used in corporate sustainability reporting?",
    "How do ESG frameworks and GRI complement each other?",
    "What role does GRI play in improving transparency in ESG reporting?",
    "How do companies map carbon emissions into GRI reporting standards?",
    "Why is Scope 3 emissions reporting challenging under GRI guidelines?",
    "How does GRI ensure consistency in sustainability disclosures?",
    "Explain how a company would use GRI to report total carbon emissions across Scope 1–3."
]

config = {
    "configurable": {
        "thread_id": "eval-session"
    }
}

BASE_DIR = Path(__file__).resolve().parent
output_file = BASE_DIR / "evaluation_results.txt"


with open(output_file, "w", encoding="utf-8") as f:

    for i, q in enumerate(questions, 1):

        result = graph.invoke(
            {"messages": [HumanMessage(content=q)]},
            config=config
        )

        answer = result["messages"][-1].content

        # simple retrieval detection
        retrieval_used = any(
            hasattr(m, "tool_calls") and m.tool_calls
            for m in result["messages"]
        )

        f.write(f"\n==============================\n")
        f.write(f"Q{i}: {q}\n")
        f.write(f"Retrieval used: {retrieval_used}\n")
        f.write(f"Answer:\n{answer}\n")

print(f"Saved results to {output_file}")