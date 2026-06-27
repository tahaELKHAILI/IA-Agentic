# Script to draw the agent graph

from src.graph.graph import graph

from pathlib import Path
from src.graph.graph import graph

BASE_DIR = Path(__file__).resolve().parent
DOCS_DIR = BASE_DIR / "graph"
PNG_PATH = DOCS_DIR / "graph.png"


def main():
    DOCS_DIR.mkdir(exist_ok=True)

    try:
        png_bytes = graph.get_graph().draw_mermaid_png()
        PNG_PATH.write_bytes(png_bytes)
        print(f"Graph PNG saved → {PNG_PATH}")

    except Exception as e:
        print("PNG generation failed:", e)
        print("Make sure graphviz is installed.")


if __name__ == "__main__":
    main()