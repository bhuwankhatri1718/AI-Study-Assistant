# 📚 AI Study Assistant — RAG-Based PDF Question Answering

An AI-powered study assistant that allows users to ask questions about PDF documents and receive context-aware answers using Retrieval-Augmented Generation (RAG).

The application processes PDF documents, splits their content into smaller chunks, converts the chunks into numerical embeddings, stores them in ChromaDB, and retrieves relevant information to generate answers using a Groq-hosted Large Language Model (LLM).

## 🚀 Features

- **PDF Document Loading:** Extract text and metadata from PDF documents.
- **Recursive Text Chunking:** Split documents while preserving paragraph and line structure.
- **Text Embeddings:** Generate vector representations using Hugging Face Sentence Transformers.
- **Vector Database:** Store and retrieve document embeddings using ChromaDB.
- **Semantic Search:** Retrieve relevant document passages based on query meaning.
- **AI-Powered Answers:** Generate context-aware answers using Groq LLM.
- **Interactive Chat Interface:** Ask questions through a Streamlit application.
- **Persistent Storage:** Save the vector database locally for reuse.
- **Source Context:** Include retrieved page information in the generation context.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| LangChain | RAG pipeline orchestration |
| PyPDFLoader | PDF document loading |
| RecursiveCharacterTextSplitter | Text chunking |
| Hugging Face | Text embedding generation |
| all-MiniLM-L6-v2 | Embedding model |
| ChromaDB | Vector database |
| Groq API | LLM inference |
| Streamlit | Web application interface |
| python-dotenv | Environment variable management |

## 🏗️ Project Architecture

```text
PDF Document
     |
     v
PDF Loading
     |
     v
Text Extraction
     |
     v
Recursive Text Chunking
     |
     v
Hugging Face Embeddings
     |
     v
ChromaDB Vector Store
     |
     v
User Question
     |
     v
Query Embedding & Similarity Search
     |
     v
Relevant Document Retrieval
     |
     v
Context + User Question
     |
     v
Groq LLM
     |
     v
Generated Answer
     |
     v
Streamlit Chat Interface
```

## 📂 Project Structure

```text
AI Study Assistant/
│
├── app.py
├── README.md
├── requirements.txt
├── .env
├── .env.example
├── .gitignore
│
├── data/
│   └── documents/
│       └── laws_of_cricket.pdf
│
├── chroma_db/
│
└── src/
    ├── __init__.py
    │
    ├── ingestion/
    │   ├── __init__.py
    │   └── pdf_loader.py
    │
    ├── processing/
    │   ├── __init__.py
    │   └── text_splitter.py
    │
    ├── embeddings/
    │   ├── __init__.py
    │   └── embedding_model.py
    │
    ├── vectorstore/
    │   ├── __init__.py
    │   └── chroma_store.py
    │
    ├── retrieval/
    │   ├── __init__.py
    │   └── retriever.py
    │
    └── generation/
        ├── __init__.py
        └── rag_chain.py
```

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-Study-Assistant.git
```

Navigate to the project directory:

```bash
cd AI-Study-Assistant
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root directory.

Add your Groq API credentials:

```env
GROQ_API_KEY=your_groq_api_key
GROQ_MODEL=openai/gpt-oss-120b
```

Get your API key from:

https://console.groq.com/keys

**Important:** Never share or commit your `.env` file or expose your API key publicly.

### 5. Add Your PDF Document

Place your PDF inside:

```text
data/documents/
```

The default document used by this project is:

```text
laws_of_cricket.pdf
```

If you use a different document, update the PDF path in `src/ingestion/pdf_loader.py`.

## ▶️ Running the Application

### Step 1: Build the Vector Database

From the project root, execute:

```bash
python -m src.vectorstore.chroma_store
```

This loads the PDF, creates chunks, generates embeddings, and stores them in ChromaDB.

### Step 2: Start the Streamlit Application

```bash
streamlit run app.py
```

Open the local URL displayed in your terminal. Usually:

```text
http://localhost:8501
```

## 💬 Example Questions

When using the cricket laws PDF, you can ask:

- What are the responsibilities of an umpire?
- What are the different ways a batsman can get out?
- Explain the rules regarding a no-ball.
- What is the role of the third umpire?
- What are the duties of the match referee?

The assistant retrieves relevant passages from the PDF and uses them to generate answers.

## 🧠 How RAG Works in This Project

**1. Document Ingestion**

PyPDFLoader extracts text and metadata from PDF pages.

**2. Text Chunking**

RecursiveCharacterTextSplitter divides extracted content into manageable chunks with overlapping context.

**3. Embedding Generation**

The `all-MiniLM-L6-v2` model converts document chunks into 384-dimensional numerical vectors.

**4. Vector Storage**

ChromaDB stores the embeddings, original text, and associated metadata.

**5. Retrieval**

When a user submits a question, the application searches ChromaDB for the most relevant document chunks using similarity search.

**6. Answer Generation**

The retrieved passages and user question are passed to a Groq-hosted LLM, which generates a context-aware response.

## 🔒 Security

- API credentials are stored in environment variables.
- `.env` is excluded from Git tracking.
- The local ChromaDB database is excluded from Git tracking.
- Private or copyrighted PDF documents should not be committed without permission.

## 🔮 Future Improvements

- Support multiple PDF uploads.
- Add document selection and management.
- Implement hybrid search using keyword and vector retrieval.
- Integrate a reranking model to improve retrieval accuracy.
- Display citations and clickable source pages.
- Add conversational memory.
- Support different embedding models.
- Implement document deletion and database updates.
- Deploy the application online.

## 👨‍💻 Author

**Bhuwan Khatri**

- GitHub: https://github.com/bhuwankhatri1718
- LinkedIn: https://www.linkedin.com/in/bhuwankhatri18/
- Email: bhuwankhatri459@gmail.com

## 📄 License

This project is intended for educational and learning purposes. Add an appropriate open-source license before permitting reuse or redistribution.