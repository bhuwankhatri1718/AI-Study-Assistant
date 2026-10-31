
import streamlit as st

from src.generation.rag_chain import answer_question
from src.vectorstore.chroma_store import create_vector_store


st.set_page_config(
    page_title="AI Study Assistant",
    page_icon="📚",
    layout="centered"
)


st.title("📚 AI Study Assistant")

st.write(
    "Ask questions about your uploaded study documents."
)


# Initialize database
@st.cache_resource
def initialize_database():
    return create_vector_store()


try:
    with st.spinner("Loading knowledge base..."):
        initialize_database()

    st.success("Knowledge base is ready!")

except Exception as e:
    st.error(f"Database initialization failed: {e}")
    st.stop()


# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []


# Display previous messages
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# User input
question = st.chat_input("Ask a question about cricket laws...")


if question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):

        with st.spinner("Searching your documents..."):

            try:
                response = answer_question(question)

                st.markdown(response)

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": response
                    }
                )

            except Exception as e:
                st.error(f"Error generating answer: {e}")
