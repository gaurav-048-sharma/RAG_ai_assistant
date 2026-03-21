from retriever import retrieve as dense_retrieve
from bm25_retriever import BM25Retriever
from reranker import Reranker

class HybridRetriever:
    def __init__(self, index, texts):
        self.index = index
        self.texts = texts
        self.bm25 = BM25Retriever(texts)
        self.reranker = Reranker()   # ✅ NEW

    def retrieve(self, query, k=5):
        # Dense search (FAISS)
        dense_results = dense_retrieve(query, self.index, self.texts, k)

        # Sparse search (BM25)
        bm25_results = self.bm25.retrieve(query, k)

        # Combine results
        combined = list(set(dense_results + bm25_results))

        # ✅ Rerank results
        reranked = self.reranker.rerank(query, combined, top_k=k)

        return reranked