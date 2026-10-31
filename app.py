
import streamlit as st

from src.generation.rag_chain import answer_question
from src.vectorstore.chroma_store import create_vector_store


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="AI Study Assistant",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)


# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown("""
<style>

/* Main application */
.stApp {
    background: #0b1020;
    color: #e5e7eb;
}

/* Hide Streamlit branding */
#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    background: transparent !important;
}

/* Main content */
.block-container {
    max-width: 1100px;
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: #111827;
    border-right: 1px solid #263247;
}

[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3 {
    color: #f9fafb;
}

/* Main title */
.main-title {
    font-size: 36px;
    font-weight: 800;
    color: #ffffff;
    margin-bottom: 5px;
}

.subtitle {
    color: #9ca3af;
    font-size: 15px;
    margin-bottom: 25px;
}

/* Hero section */
.hero {
    background: linear-gradient(
        135deg,
        #182747,
        #29205a
    );
    padding: 28px;
    border-radius: 18px;
    border: 1px solid #37446b;
    margin-bottom: 25px;
}

.hero h2 {
    color: white;
    font-size: 25px;
    margin-bottom: 8px;
}

.hero p {
    color: #cbd5e1;
    margin-bottom: 0;
}

/* Info cards */
.info-card {
    background: #151e30;
    border: 1px solid #29364e;
    border-radius: 14px;
    padding: 18px;
    min-height: 110px;
}

.info-card h3 {
    color: #a78bfa;
    font-size: 14px;
    margin-bottom: 8px;
}

.info-card p {
    color: #f8fafc;
    font-size: 18px;
    font-weight: 600;
    margin: 0;
}

/* Chat messages */
[data-testid="stChatMessage"] {
    background: #151e30;
    border: 1px solid #29364e;
    border-radius: 14px;
    padding: 15px;
    margin-bottom: 14px;
}

/* Chat input */
[data-testid="stChatInput"] {
    border: 1px solid #475569;
    border-radius: 14px;
}

/* Buttons */
.stButton > button {
    border-radius: 10px;
    border: 1px solid #475569;
    background: #1e293b;
    color: white;
    padding: 10px 15px;
    transition: 0.2s;
}

.stButton > button:hover {
    border-color: #a78bfa;
    color: #c4b5fd;
}

/* Divider */
hr {
    border-color: #29364e;
}

/* Footer */
.custom-footer {
    text-align: center;
    color: #64748b;
    font-size: 13px;
    padding: 25px 0 5px 0;
}

</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# DATABASE INITIALIZATION
# --------------------------------------------------

@st.cache_resource
def initialize_database():
    return create_vector_store()


try:
    with st.spinner("Initializing your knowledge base..."):
        initialize_database()

except Exception as e:
    st.error(f"Database initialization failed: {e}")
    st.stop()


# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

if "question_count" not in st.session_state:
    st.session_state.question_count = 0


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

with st.sidebar:

    st.markdown("# 📚 StudyAI")

    st.caption("YOUR PERSONAL AI LEARNING COMPANION")

    st.divider()

    st.markdown("### 💬 Workspace")

    if st.button("＋ New Chat", use_container_width=True):
        st.session_state.messages = []
        st.session_state.question_count = 0
        st.rerun()

    st.markdown("### 📖 Knowledge Base")

    st.markdown("""
    <div class="info-card">
        <h3>ACTIVE DOCUMENT</h3>
        <p>🏏 Laws of Cricket</p>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    st.markdown("### ⚙️ About")

    st.caption(
        "Powered by LangChain, ChromaDB, "
        "Hugging Face and Groq."
    )

    st.divider()

    st.markdown("### 🧠 RAG Pipeline")

    st.markdown("""
    - 📄 PDF Loading
    - ✂️ Text Chunking
    - 🔢 Embeddings
    - 🗄️ Vector Storage
    - 🔍 Retrieval
    - 🤖 AI Generation
    """)

    st.divider()

    st.caption("AI Study Assistant • Version 1.0")


# --------------------------------------------------
# MAIN HEADER
# --------------------------------------------------

st.markdown(
    '<div class="main-title">AI Study Assistant ✨</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Your intelligent companion for understanding study materials.'
    '</div>',
    unsafe_allow_html=True
)


# --------------------------------------------------
# HERO SECTION
# --------------------------------------------------

st.markdown("""
<div class="hero">
    <h2>Learn smarter. Understand faster. 🚀</h2>
    <p>
        Ask questions about your documents and get
        AI-generated answers based on their content.
    </p>
</div>
""", unsafe_allow_html=True)


# --------------------------------------------------
# STATISTICS
# --------------------------------------------------

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="info-card">
        <h3>📚 DOCUMENT</h3>
        <p>Laws of Cricket</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="info-card">
        <h3>🤖 AI ENGINE</h3>
        <p>Groq LLM</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="info-card">
        <h3>💬 QUESTIONS ASKED</h3>
        <p>{st.session_state.question_count}</p>
    </div>
    """, unsafe_allow_html=True)


st.write("")
st.markdown("### 💡 Suggested Questions")

# --------------------------------------------------
# SUGGESTED QUESTIONS
# --------------------------------------------------

suggestions = [
    "What are the different ways a batsman can get out?",
    "What are the responsibilities of an umpire?",
    "Explain the rules regarding a no-ball.",
    "What is the role of the third umpire?"
]

col1, col2 = st.columns(2)

if "selected_question" not in st.session_state:
    st.session_state.selected_question = None

with col1:
    if st.button(suggestions[0], use_container_width=True):
        st.session_state.selected_question = suggestions[0]

    if st.button(suggestions[1], use_container_width=True):
        st.session_state.selected_question = suggestions[1]

with col2:
    if st.button(suggestions[2], use_container_width=True):
        st.session_state.selected_question = suggestions[2]

    if st.button(suggestions[3], use_container_width=True):
        st.session_state.selected_question = suggestions[3]


st.divider()

st.markdown("### 💬 Conversation")


# --------------------------------------------------
# DISPLAY CHAT HISTORY
# --------------------------------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])


# --------------------------------------------------
# PROCESS USER QUESTION
# --------------------------------------------------

question = st.chat_input(
    "Ask anything about your study document..."
)

if st.session_state.selected_question:

    question = st.session_state.selected_question
    st.session_state.selected_question = None


if question:

    # Display user question
    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    with st.chat_message("user"):
        st.markdown(question)

    # Generate AI response
    with st.chat_message("assistant"):

        with st.spinner("🔍 Searching documents and generating answer..."):

            try:

                response = answer_question(question)

                st.markdown(response)

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": response
                })

                st.session_state.question_count += 1

            except Exception as e:

                error_message = f"Unable to generate an answer: {e}"

                st.error(error_message)

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": error_message
                })

    st.rerun()


# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown("""
<div class="custom-footer">
    Built with ❤️ using Python, LangChain, ChromaDB and Streamlit
    <br>
    AI Study Assistant • Learn without limits
</div>
""", unsafe_allow_html=True)
