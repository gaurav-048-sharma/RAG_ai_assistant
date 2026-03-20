from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

def create_embeddings(docs):
    texts = [doc.page_content for doc in docs]
    embeddings = model.encode(texts)
    return embeddings, texts