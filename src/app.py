import os
from loader import load_documents
from chunker import split_documents
from embedder import create_embeddings
from vectorstore import create_faiss_index, save_index, load_index
from retriever import retrieve
from generator import generate_answer

# If index exists → load
if os.path.exists("faiss_index.bin"):
    print("Loading existing index...")
    index, texts = load_index()
else:
    print("Creating new index...")

    docs = load_documents("data")
    chunks = split_documents(docs)

    embeddings, texts = create_embeddings(chunks)
    index = create_faiss_index(embeddings)

    save_index(index, texts)

    print("✅ Index created successfully!")

# Chat loop
while True:
    query = input("\nAsk something: ")

    results = retrieve(query, index, texts)
    context = "\n".join(results)

    # 🔍 Debug (IMPORTANT)
    print("\n--- Retrieved Context ---\n")
    print(context[:500])  # first 500 chars
    print("\n------------------------\n")

    answer = generate_answer(query, context)

    print("\nAnswer:", answer)
# from loader import load_documents
# from chunker import split_documents
# from embedder import create_embeddings
# from vectorstore import create_faiss_index
# from retriever import retrieve
# from generator import generate_answer

# # Load + process
# docs = load_documents("data")
# chunks = split_documents(docs)
# embeddings, texts = create_embeddings(chunks)
# index = create_faiss_index(embeddings)

# # Query loop
# while True:
#     query = input("Ask something: ")
    
#     results = retrieve(query, index, texts)
#     context = "\n".join(results)
    
#     answer = generate_answer(query, context)
    
#     print("\nAnswer:", answer)