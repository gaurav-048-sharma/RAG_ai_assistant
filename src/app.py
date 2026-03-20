from loader import load_documents
from chunker import split_documents
from embedder import create_embeddings
from vectorstore import create_faiss_index
from retriever import retrieve
from generator import generate_answer

# Load + process
docs = load_documents("data/sample.pdf")
chunks = split_documents(docs)
embeddings, texts = create_embeddings(chunks)
index = create_faiss_index(embeddings)

# Query loop
while True:
    query = input("Ask something: ")
    
    results = retrieve(query, index, texts)
    context = "\n".join(results)
    
    answer = generate_answer(query, context)
    
    print("\nAnswer:", answer)