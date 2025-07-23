from embeddings import embeddings
from langchain_community.vectorstores import Chroma

def vector_database(chunks):
    embedding_model = embeddings()
    vector_database = Chroma.from_documents(chunks, embedding_model)
    return vector_database