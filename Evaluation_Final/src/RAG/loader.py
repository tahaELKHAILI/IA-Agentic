# This script load the files in resources file

from pathlib import Path
import sys
from langchain_community.document_loaders import PyPDFLoader, TextLoader, Docx2txtLoader

sys.path.append(str(Path(__file__).resolve().parents[2]))


from config.config import DATA_DIR

# The data files for the RAG are located in resources
# Files are organised on the basis of type: PDF, DOC, TXT etc....

# This function prepare the pasth to all the files and store them in an array
def loadFiles():
    filesPaths = []

    for directory in DATA_DIR.iterdir():
        if directory.is_dir():
            for file in directory.iterdir():
                if file.is_file():
                    filesPaths.append(file)

    return filesPaths


# This function reads the files
def readFiles(paths):
    output = []
    for path in paths:
        extension = Path(path).suffix
        if(extension == ".pdf"):
            loader = PyPDFLoader(path)
        elif(extension == ".txt"):
            loader = TextLoader(path)
        elif(extension == ".docx"):
            loader = Docx2txtLoader(path)
        else:
            print(f"Unsuported file type {extension}")

        data = loader.load()
        output.extend(data)

    return output


filesPaths = loadFiles()

if not filesPaths:
    print("Error, no file found")
else:
    RAG_Data = readFiles(filesPaths)
    print("All data was loaded")
