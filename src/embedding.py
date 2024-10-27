from sentence_transformers import SentenceTransformer
from langchain_core.embeddings import Embeddings

class SentenceTransformerEmbeddings(Embeddings):
    def __init__(self, model_name: str):
        self.model = SentenceTransformer(model_name)

    def embed_documents(self, texts):
        embeddings = self.model.encode(texts)
        return embeddings
    
    def embed_query(self, text):
        embeddings = self.model.encode(text)
        return embeddings