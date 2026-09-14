from sentence_transformers import SentenceTransformer


model = SentenceTransformer("all-MiniLM-L6-v2")


texts = [
    "I have experience with Python and Django.",
    "I have worked on backend web applications.",
    "I enjoy eating pizza."
]


embeddings = model.encode(texts)


for i, embedding in enumerate(embeddings):
    print(f"\nText {i + 1}:")
    print(texts[i])

    print("Vector dimensions:", len(embedding))
    print("First 10 values:", embedding[:10])