from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

DATA_PATH = Path("data")

documents = []

# Load PDFs
for pdf_file in DATA_PATH.rglob("*.pdf"):
    print(f"Loading: {pdf_file}")
    loader = PyPDFLoader(str(pdf_file))
    documents.extend(loader.load())

print(f"\nDocuments Loaded: {len(documents)}")

# Split Documents
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,
    chunk_overlap=150
)

chunks = text_splitter.split_documents(documents)

print(f"Chunks Created: {len(chunks)}")

# Embedding Model
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Save to ChromaDB
vector_store = Chroma.from_documents(
    documents=chunks,
    embedding=embedding_model,
    persist_directory="chroma_db"
)

print("\n=================================")
print("Documents successfully stored in ChromaDB.")
print("=================================")