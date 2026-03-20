import faiss
import numpy as np
import pickle
import os

# Always save in ROOT folder
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

INDEX_PATH = os.path.join(BASE_DIR, "faiss_index.bin")
TEXT_PATH = os.path.join(BASE_DIR, "texts.pkl")

def create_faiss_index(embeddings):
    dim = len(embeddings[0])
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings))
    return index

def save_index(index, texts):
    faiss.write_index(index, INDEX_PATH)
    with open(TEXT_PATH, "wb") as f:
        pickle.dump(texts, f)

    print("✅ Index saved at:", INDEX_PATH)
    print("✅ Texts saved at:", TEXT_PATH)

def load_index():
    if not os.path.exists(INDEX_PATH) or not os.path.exists(TEXT_PATH):
        raise FileNotFoundError("FAISS index not found. Run app.py first.")

    index = faiss.read_index(INDEX_PATH)

    with open(TEXT_PATH, "rb") as f:
        texts = pickle.load(f)

    return index, texts
# # import faiss
# # import numpy as np

# # def create_faiss_index(embeddings):
# #     dim = len(embeddings[0])
# #     index = faiss.IndexFlatL2(dim)
# #     index.add(np.array(embeddings))
# #     return index

# import faiss
# import numpy as np
# import pickle
# import os

# def create_faiss_index(embeddings):
#     dim = len(embeddings[0])
#     index = faiss.IndexFlatL2(dim)
#     index.add(np.array(embeddings))
#     return index

# def save_index(index, texts):
#     faiss.write_index(index, "faiss_index.bin")
#     with open("texts.pkl", "wb") as f:
#         pickle.dump(texts, f)

# def load_index():
#     if not os.path.exists("faiss_index.bin") or not os.path.exists("texts.pkl"):
#         raise FileNotFoundError("FAISS index not found. Run app.py first to create it.")

#     index = faiss.read_index("faiss_index.bin")

#     with open("texts.pkl", "rb") as f:
#         texts = pickle.load(f)

#     return index, texts