from sentence_transformers import SentenceTransformer

from rag.ingestion import load_pdf
from rag.chunking import chunk_text
from rag.vector_store import VectorStore


PDF_PATH = "data/documents/Resume-DevasheeshP.pdf.pdf"


# 1. Load PDF
text = load_pdf(PDF_PATH)


# 2. Chunk document
chunks = chunk_text(
    text,
    chunk_size=500,
    chunk_overlap=50,
)


# 3. Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


# 4. Create embeddings
embeddings = model.encode(chunks)


# 5. Create metadata
metadatas = [
    {
        "source": "Resume-DevasheeshP.pdf.pdf",
        "chunk_id": i,
    }
    for i in range(len(chunks))
]


# 6. Create IDs
ids = [
    f"resume_chunk_{i}"
    for i in range(len(chunks))
]


# 7. Create vector store
vector_store = VectorStore()


# 8. Store everything
vector_store.add_documents(
    documents=chunks,
    embeddings=embeddings,
    metadatas=metadatas,
    ids=ids,
)


print(f"Stored {len(chunks)} chunks in ChromaDB.")