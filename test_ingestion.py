from rag.ingestion import load_pdf
from rag.chunking import chunk_text


pdf_path = "data/documents/Resume-DevasheeshP.pdf.pdf"

text = load_pdf(pdf_path)

print("Total characters:", len(text))

chunks = chunk_text(
    text,
    chunk_size=500,
    chunk_overlap=50,
)

print("Total chunks:", len(chunks))

for i, chunk in enumerate(chunks[:5]):
    print(f"\n--- Chunk {i + 1} ---")
    print(chunk)