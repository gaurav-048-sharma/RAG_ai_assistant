# 🧠 RAG AI Assistant (Chat with Your Documents)

A production-style Retrieval-Augmented Generation (RAG) system that allows users to query and interact with their own documents (PDFs) using semantic search and a local Large Language Model (LLM).

---

## 🚀 Features

- 📄 Load and process multiple PDF documents
- ✂️ Intelligent text chunking using RecursiveCharacterTextSplitter
- 🧠 Semantic search using embeddings (Sentence Transformers)
- 🗄️ Vector database powered by FAISS
- 🔍 Context-aware retrieval system
- 🤖 Response generation using local LLM (LLaMA 3 via Ollama)
- 💻 Fully local execution (no API cost)

---

## 🏗️ Project Architecture

---

## ⚙️ Tech Stack

- **Language:** Python  
- **Embeddings:** Sentence Transformers (`all-MiniLM-L6-v2`)  
- **Vector DB:** FAISS  
- **LLM:** LLaMA 3 (via Ollama)  
- **Libraries:** LangChain, HuggingFace, Requests  

---

## 🔄 How It Works (RAG Pipeline)

1. **Document Loading**
   - PDFs are loaded from the `data/` folder

2. **Chunking**
   - Documents are split into smaller chunks for better retrieval

3. **Embedding**
   - Each chunk is converted into vector embeddings

4. **Vector Storage**
   - Embeddings are stored in FAISS index

5. **Query Processing**
   - User query is converted into embedding

6. **Retrieval**
   - Top relevant chunks are retrieved using similarity search

7. **Generation**
   - Retrieved context + query → sent to LLM → final answer generated

---

## 🛠️ Installation & Setup

### 1. Clone the repository

- https://github.com/gaurav-048-sharma/RAG_ai_assistant.git
- cd rag-ai-assistant

### 2. Create virtual environment


- python -m venv venv
- venv\Scripts\activate # Windows


### 3. Install dependencies


- pip install -r requirements.txt


---

## 🤖 Setup Ollama (Local LLM)

1. Download Ollama: https://ollama.com  
2. Install and restart terminal  
3. Run:


---

## ▶️ Run the Application
- python src/app.py


---

## 💡 Example Queries

- What is machine learning?
- Explain neural networks
- What is overfitting?
- Compare supervised and unsupervised learning

---

## 📊 Key Highlights

- Built end-to-end RAG pipeline using FAISS and embeddings  
- Enabled semantic document search with context-aware responses  
- Reduced dependency on external APIs using local LLM  
- Designed modular architecture for scalability  

---

## 🚀 Future Improvements

- Add Streamlit UI (ChatGPT-like interface)
- Implement hybrid search (BM25 + embeddings)
- Add reranking for better retrieval accuracy
- Add chat history and memory
- Deploy on cloud (AWS / Docker)

---

## 🧠 Learning Outcomes

- Deep understanding of RAG architecture
- Working with embeddings and vector databases
- LLM integration and prompt engineering
- Building production-style AI systems

---

## 📌 Author

**Gaurav Sharma**  
GitHub: https://github.com/gaurav-048-sharma  
LinkedIn: https://linkedin.com/in/gaurav-sharma-a8568a199  
