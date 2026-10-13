
from sentence_transformers import SentenceTransformer
import chromadb

# Load the embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Connect to the existing ChromaDB database
client = chromadb.PersistentClient(path="chroma_db")
collection = client.get_collection(name="research_documents")


# Tool 1: Search the research paper
def search_documents(query):
    query_embedding = model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3
    )

    documents = results["documents"][0]
    return "\n\n".join(documents)


# Tool 2: Calculator
def calculator(expression):
    try:
        result = eval(expression)
        return str(result)
    except Exception:
        return "Invalid calculation"
