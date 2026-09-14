from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


model = SentenceTransformer("all-MiniLM-L6-v2")


texts = [
    "I have experience with Python and Django.",
    "I have worked on backend web applications.",
    "I enjoy eating pizza.",
]


embeddings = model.encode(texts)


similarity_1_2 = cosine_similarity(
    [embeddings[0]],
    [embeddings[1]]
)[0][0]

similarity_1_3 = cosine_similarity(
    [embeddings[0]],
    [embeddings[2]]
)[0][0]


print("Text 1:", texts[0])
print("Text 2:", texts[1])
print("Similarity:", similarity_1_2)

print("\nText 1:", texts[0])
print("Text 3:", texts[2])
print("Similarity:", similarity_1_3)