
import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from src.retrieval.retriever import retrieve_documents


load_dotenv()


def get_llm():

    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise ValueError("GROQ_API_KEY is missing from .env")

    model_name = os.getenv(
        "GROQ_MODEL",
        "openai/gpt-oss-120b"
    )

    llm = ChatGroq(
        model=model_name,
        temperature=0
    )

    return llm


def answer_question(question):

    documents = retrieve_documents(question)

    if not documents:
        return "I couldn't find relevant information in the PDF."

    context = "\n\n".join(
        [
            f"Source page: {doc.metadata.get('page', 'Unknown')}\n"
            f"{doc.page_content}"
            for doc in documents
        ]
    )

    prompt = ChatPromptTemplate.from_template(
        """
        You are an AI Study Assistant.

        Answer the question using only the provided context.

        If the answer is not available in the context,
        clearly say that the PDF does not provide enough information.

        Explain the answer clearly and simply.

        Context:
        {context}

        Question:
        {question}

        Answer:
        """
    )

    llm = get_llm()

    chain = prompt | llm | StrOutputParser()

    response = chain.invoke(
        {
            "context": context,
            "question": question
        }
    )

    return response


if __name__ == "__main__":

    question = "What are the responsibilities of an umpire?"

    response = answer_question(question)

    print("\nAI Answer:\n")
    print(response)
