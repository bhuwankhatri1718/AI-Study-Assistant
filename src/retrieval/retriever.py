
from src.vectorstore.chroma_store import create_vector_store


def retrieve_documents(question, k=4):

    vector_store = create_vector_store()

    retriever = vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={"k": k}
    )

    relevant_documents = retriever.invoke(question)

    return relevant_documents


if __name__ == "__main__":

    question = "What are the responsibilities of an umpire?"

    documents = retrieve_documents(question)

    for i, document in enumerate(documents):

        print(f"\nDocument {i + 1}")
        print(document.page_content)
        print("Metadata:", document.metadata)
