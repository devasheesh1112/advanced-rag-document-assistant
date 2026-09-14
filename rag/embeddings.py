import os

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def create_embedding(text: str) -> list[float]:
    """
    Generate an embedding vector for the given text.
    """

    if not text.strip():
        raise ValueError("Text cannot be empty.")

    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text,
    )

    return response.data[0].embedding