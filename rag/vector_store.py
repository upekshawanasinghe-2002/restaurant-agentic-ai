from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

# Embedding model
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Create / Load Chroma database
vector_store = Chroma(
    persist_directory="chroma_db",
    embedding_function=embedding_model
)

print("Chroma Vector Store initialized successfully.")