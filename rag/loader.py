from langchain_community.document_loaders import PyPDFLoader
from pathlib import Path

# Data folder path
DATA_PATH = Path("data")

documents = []

# Search all PDF files inside data/
for pdf_file in DATA_PATH.rglob("*.pdf"):
    print(f"Loading: {pdf_file}")

    loader = PyPDFLoader(str(pdf_file))
    docs = loader.load()

    documents.extend(docs)

print("\n---------------------------")
print(f"Total Documents Loaded: {len(documents)}")
print("---------------------------")