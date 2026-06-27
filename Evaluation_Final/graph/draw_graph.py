# Script to draw the agent graph
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.graph.graph import graph

BASE_DIR = Path(__file__).resolve().parents[1]
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


if __name__ == "__main__":
    main()

