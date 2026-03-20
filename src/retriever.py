from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

def retrieve(query, index, texts, k=3):
    query_vec = model.encode([query])
    D, I = index.search(query_vec, k)
    
    results = [texts[i] for i in I[0]]
    return results