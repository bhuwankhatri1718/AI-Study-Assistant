from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader


# Get the project root directory
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# Define the PDF file path
PDF_PATH = PROJECT_ROOT / "data" / "documents" / "laws_of_cricket.pdf"


def load_pdf():
    """Load PDF pages as LangChain Document objects."""

    # Check whether the PDF exists
    if not PDF_PATH.exists():
        raise FileNotFoundError(
            f"PDF file not found: {PDF_PATH}"
        )

    # Initialize the PDF loader
    loader = PyPDFLoader(str(PDF_PATH))

    # Load all pages
    documents = loader.load()

    print(f"PDF loaded successfully!")
    print(f"Total pages: {len(documents)}")

    # Display first page content
    if documents:
        print("\nFirst page content:\n")
        print(documents[0].page_content)

        print("\nFirst page metadata:")
        print(documents[0].metadata)

    return documents


if __name__ == "__main__":
    docs = load_pdf()