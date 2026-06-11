# TP Prompt Engineering
This project contain practice elements from the course covering the topics of tokenisation and prompting
## Contenu
* `01_Tokenisation.py`: Tokenisation using `Tiktoken`
* `02_OllamaPrompt.py`: Prompt using `Ollama`
* `03_GroqPrompt.py`: Prompt using `Groq`
* `04_OpenAIPrompt.py`: Prompt using `OpenAI`
* `05_OpenAISentiment.py`: Sentiment analysis using `OpenAI` with JSON output
* `06_ImageGeneration.py`: Image generation using `OpenAI`
* `07_ImageDescription.py`: Description of an image using `OpenAI` src = `rag.png`
## Environnement file
        MODEL_OLLAMA = llama3.2:latest
        GROQ_API_KEY = --Insert your API Key--
        OPENAI_API_KEY = --Insert your API Key--
## UV setup
        uv venv -- to create your project's virtual environnement
        uv sync -- synchronizes your project’s virtual environment with your exact dependency specifications
## Dependencies
        python = ">=3.14
        langchain>=1.3.7
        langchain-community>=0.4.2
        langchain-groq>=1.1.3
        langchain-ollama>=1.1.0
        langchain-openai>=1.3.0
        tiktoken>=0.13.0
## Execution
        python *Insert script name*.py
        Example. python 01_Tokenisation.py
## Notes
* `02_OllamaPrompt.py` require an active ollama server with a local model.
* From `03` to `07` you need valid API keys for Groq and OpenAI