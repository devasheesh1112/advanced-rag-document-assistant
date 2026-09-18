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