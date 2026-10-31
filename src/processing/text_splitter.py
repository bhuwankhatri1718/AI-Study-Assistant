
from langchain_text_splitters import RecursiveCharacterTextSplitter
from src.ingestion.pdf_loader import load_pdf


def split_documents():

    # Step 1: Load PDF documents
    documents = load_pdf()

    # Step 2: Create structure-based splitter
    splitter = RecursiveCharacterTextSplitter(
        separators=["\n\n", "\n", " ", ""],
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len,
    )

    # Step 3: Split documents
    chunks = splitter.split_documents(documents)

    # Step 4: Display results
    print(f"\nTotal chunks: {len(chunks)}")

    for i, chunk in enumerate(chunks[:5]):
        print(f"\nChunk {i + 1}")
        print("Content:", repr(chunk.page_content))
        print("Metadata:", chunk.metadata)
        print("Length:", len(chunk.page_content))

    return chunks


if __name__ == "__main__":
    chunks = split_documents()
