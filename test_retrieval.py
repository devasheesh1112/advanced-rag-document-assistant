from sentence_transformers import SentenceTransformer

from rag.ingestion import load_pdf
from rag.chunking import chunk_text
from rag.retrieval import retrieve


PDF_PATH = "data/documents/Resume-DevasheeshP.pdf.pdf"


# 1. Load PDF
text = load_pdf(PDF_PATH)


# 2. Create chunks
chunks = chunk_text(
    text,
    chunk_size=500,
    chunk_overlap=50,
)


# 3. Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


# 4. Create embeddings for all chunks
embeddings = model.encode(chunks)


# 5. User query
query = "Does the candidate have Python experience?"


# 6. Create query embedding
query_embedding = model.encode([query])[0]


# 7. Retrieve top 3 chunks
results = retrieve(
    query=query,
    chunks=chunks,
    embeddings=embeddings,
    query_embedding=query_embedding,
    top_k=3,
)


# 8. Display results
print(f"\nQuery: {query}\n")

for rank, (chunk, score) in enumerate(results, start=1):
    print("=" * 80)
    print(f"Rank: {rank}")
    print(f"Similarity Score: {score:.4f}")
    print("\nChunk:")
    print(chunk)