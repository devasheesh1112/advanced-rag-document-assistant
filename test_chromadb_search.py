from sentence_transformers import SentenceTransformer

from rag.vector_store import VectorStore


model = SentenceTransformer("all-MiniLM-L6-v2")

query = "Does the candidate have Python experience?"

query_embedding = model.encode(query)


vector_store = VectorStore()

results = vector_store.search(
    query_embedding=query_embedding,
    top_k=3,
)


documents = results["documents"][0]
distances = results["distances"][0]
metadatas = results["metadatas"][0]


print(f"\nQuery: {query}\n")


for i, (document, distance, metadata) in enumerate(
    zip(documents, distances, metadatas),
    start=1,
):
    print("=" * 80)

    print(f"Rank: {i}")

    print(f"Distance: {distance:.4f}")

    print(f"Source: {metadata['source']}")

    print(f"Chunk ID: {metadata['chunk_id']}")

    print("\nDocument:")
    print(document)