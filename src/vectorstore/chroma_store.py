
from langchain_chroma import Chroma

from src.processing.text_splitter import split_documents
from src.embeddings.embedding_model import get_embedding_model


# Database location
PERSIST_DIRECTORY = "./chroma_db"

# Collection name
COLLECTION_NAME = "cricket_laws"


def create_vector_store():
    """Create and persist the ChromaDB vector store."""

    # Step 1: Load the embedding model
    embedding_model = get_embedding_model()

    # Step 2: Load and split PDF documents
    chunks = split_documents()

    # Step 3: Create Chroma vector store
    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        collection_name=COLLECTION_NAME,
        persist_directory=PERSIST_DIRECTORY,
    )

    print("\nVector database created successfully!")
    print("Total chunks stored:", vector_store._collection.count())
    print("Database location:", PERSIST_DIRECTORY)

    return vector_store


if __name__ == "__main__":
    db = create_vector_store()
