
from langchain_huggingface import HuggingFaceEmbeddings


def get_embedding_model():
    """Initialize and return the Hugging Face embedding model."""

    embedding_model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    return embedding_model


if __name__ == "__main__":

    # Initialize embedding model
    embeddings = get_embedding_model()

    # Generate embedding for a sample sentence
    sample_text = "Cricket is a bat and ball sport."

    vector = embeddings.embed_query(sample_text)

    # Display results
    print("Embedding generated successfully!")
    print("Vector dimensions:", len(vector))
    print("First 10 values:", vector[:10])
