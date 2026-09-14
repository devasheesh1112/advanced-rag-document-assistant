from rag.ingestion import load_pdf
from rag.chunking import chunk_text
from rag.embeddings import create_embedding


pdf_path = "data/documents/Resume-DevasheeshP.pdf.pdf"

text = load_pdf(pdf_path)

chunks = chunk_text(
    text,
    chunk_size=500,
    chunk_overlap=50,
)

first_chunk = chunks[0]

embedding = create_embedding(first_chunk)

print("Chunk length:", len(first_chunk))
print("Embedding dimensions:", len(embedding))

print("\nFirst 10 values:")
print(embedding[:10])