from sklearn.metrics.pairwise import cosine_similarity


def retrieve(
    query: str,
    chunks: list[str],
    embeddings,
    query_embedding,
    top_k: int = 3,
):
    """
    Retrieve the most relevant chunks for a query.
    """

    scores = cosine_similarity(
        [query_embedding],
        embeddings
    )[0]

    ranked_results = sorted(
        zip(chunks, scores),
        key=lambda item: item[1],
        reverse=True,
    )

    return ranked_results[:top_k]
