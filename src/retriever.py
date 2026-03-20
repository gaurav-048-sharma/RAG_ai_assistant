from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

def retrieve(query, index, texts, k=5):
    query_vec = model.encode(query, convert_to_tensor=True)

    # Step 1: Get more candidates
    D, I = index.search(model.encode([query]), k*2)

    candidates = [texts[i] for i in I[0]]

    # Step 2: Rerank using similarity
    scores = []
    for text in candidates:
        score = util.cos_sim(query_vec, model.encode(text, convert_to_tensor=True))
        scores.append(score.item())

    # Step 3: Sort by score
    ranked = sorted(zip(candidates, scores), key=lambda x: x[1], reverse=True)

    # Step 4: Return top-k
    results = [text for text, _ in ranked[:k]]

    return results

# from sentence_transformers import SentenceTransformer

# model = SentenceTransformer('all-MiniLM-L6-v2')

# def retrieve(query, index, texts, k=3):
#     query_vec = model.encode([query])
#     D, I = index.search(query_vec, k)
    
#     results = [texts[i] for i in I[0]]
#     return results