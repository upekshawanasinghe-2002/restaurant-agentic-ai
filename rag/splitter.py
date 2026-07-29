from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

DATA_PATH = Path("data")

documents = []

for pdf_file in DATA_PATH.rglob("*.pdf"):
    loader = PyPDFLoader(str(pdf_file))
    documents.extend(loader.load())

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,
    chunk_overlap=150
)

chunks = text_splitter.split_documents(documents)

print(f"Documents Loaded : {len(documents)}")
print(f"Chunks Created   : {len(chunks)}")

print("\nFirst Chunk Preview:\n")
print(chunks[0].page_content[:500])