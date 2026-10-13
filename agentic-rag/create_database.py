
from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
import chromadb

# Read the research paper
pdf_path = "documents/research_paper.pdf"
reader = PdfReader(pdf_path)

full_text = ""

for page in reader.pages:
    full_text += (page.extract_text() or "") + "\n"

print("PDF text extracted successfully.")

# Split the text into chunks
chunk_size = 500
chunks = []

for i in range(0, len(full_text), chunk_size):
    chunk = full_text[i:i + chunk_size]
    if chunk.strip():
        chunks.append(chunk)

print("Number of chunks:", len(chunks))

if not chunks:
    raise ValueError("No text found in the PDF. Please check your PDF file.")

# Create embeddings
model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = model.encode(chunks).tolist()

print("Embeddings created.")

# Store the embeddings in ChromaDB
client = chromadb.PersistentClient(path="chroma_db")
collection = client.get_or_create_collection(
    name="research_documents"
)

# Clear old data before rebuilding the database
if collection.count() > 0:
    client.delete_collection(name="research_documents")
    collection = client.create_collection(name="research_documents")

collection.add(
    ids=[str(i) for i in range(len(chunks))],
    documents=chunks,
    embeddings=embeddings
)

print("Database created successfully!")
print("Documents stored:", collection.count())
