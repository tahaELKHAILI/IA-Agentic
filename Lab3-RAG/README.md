# TP RAG Implementation
Implement the RAG pattern (augmentation generation with recovery) with LangChain to allow the LLM agent to respond to questions on other sources: a PDF file and a SQL database.
## Contenu
* `01_Part1_RAG_PDF.py` RAG Agent on a PDF
* `02_Part2_SQL_Agent.py` Agent SQL sur SQLite
* `resources` containt the PDF file used for the RAG and the music database file
## Environnement file
        MODEL_OLLAMA = llama3.2:latest
        
## UV setup
        uv venv -- to create your project's virtual environnement
        uv sync -- synchronizes your project’s virtual environment with your exact dependency specifications
## Dependencies
        python = >=3.14
        langchain>=1.3.9
        langchain-community>=0.4.2
        langchain-ollama>=1.1.0
        pypdf>=6.13.2
        sentence-transformers>=5.5.1
## Execution
        python *Insert script name*.py
        Example. python Lab_Agent_WithMemory.py
## Notes
* The scripts require an active ollama server with a local model.
