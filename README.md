# 📚 Advanced RAG Document Assistant

A modular **Retrieval-Augmented Generation (RAG)** document assistant built with **Django, Python, ChromaDB, Sentence Transformers, and LLMs**.

The project focuses on building a production-oriented RAG pipeline for document ingestion, text processing, embeddings, vector storage, semantic retrieval, and AI-powered question answering.

---

## 🚀 Features

- 📄 Document ingestion and text extraction
- ✂️ Text chunking
- 🧠 Local embedding generation
- 🔎 Semantic similarity search
- 🗄️ ChromaDB vector storage
- 🎯 Context-aware document retrieval
- 🤖 LLM-powered question answering
- 🌐 Django-based backend architecture
- 🧪 Modular testing for RAG components

---

## 🏗️ Architecture

```text
                    Documents
                        │
                        ▼
                ┌───────────────┐
                │   Ingestion   │
                └───────┬───────┘
                        │
                        ▼
                ┌───────────────┐
                │   Chunking    │
                └───────┬───────┘
                        │
                        ▼
                ┌───────────────┐
                │   Embeddings  │
                └───────┬───────┘
                        │
                        ▼
                ┌───────────────┐
                │   ChromaDB    │
                │ Vector Store  │
                └───────┬───────┘
                        │
                        ▼
                 User Question
                        │
                        ▼
                ┌───────────────┐
                │   Retrieval   │
                └───────┬───────┘
                        │
                        ▼
                Relevant Context
                        │
                        ▼
                ┌───────────────┐
                │      LLM      │
                └───────┬───────┘
                        │
                        ▼
                    AI Answer



Document
   │
   ▼
Text Extraction
   │
   ▼
Text Cleaning
   │
   ▼
Chunking
   │
   ▼
Embedding Generation
   │
   ▼
Vector Storage
   │
   ▼
User Query
   │
   ▼
Query Embedding
   │
   ▼
Similarity Search
   │
   ▼
Relevant Chunks
   │
   ▼
LLM
   │
   ▼
Final Answer




advanced-rag-document-assistant/
│
├── config/
│   └── Django project configuration
│
├── rag/
│   ├── ingestion.py
│   ├── embeddings.py
│   ├── chunking.py
│   ├── retrieval.py
│   ├── vector_store.py
│   └── views.py
│
├── data/
│   └── documents/
│
├── tests/
│
├── chroma_db/
│
├── manage.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md



User Query
    │
    ▼
Query Embedding
    │
    ▼
Vector Similarity Search
    │
    ▼
Top Relevant Chunks
    │
    ▼
Retrieved Context