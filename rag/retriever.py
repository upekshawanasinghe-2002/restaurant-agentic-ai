from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

# Load embedding model
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Load existing ChromaDB
vector_store = Chroma(
    persist_directory="chroma_db",
    embedding_function=embedding_model
)

# Create retriever
retriever = vector_store.as_retriever(search_kwargs={"k": 5})

# Test query
query = "Best seafood restaurants in Galle"

results = retriever.invoke(query)

print(f"\nQuery: {query}\n")

for i, doc in enumerate(results, start=1):
    print("=" * 60)
    print(f"Result {i}")
    print(doc.page_content[:500])