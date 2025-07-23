from embeddings import get_embeddings

from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS

def create_database(pdf_file):
    loader = PyPDFLoader(pdf_file)

    docs = loader.load()

    documents = RecursiveCharacterTextSplitter(
        chunk_size=1000, separators=["\n","\n\n"], chunk_overlap=200
    ).split_documents(docs)

    embeddings = get_embeddings()

    db = FAISS.from_documents(
        documents=documents,
        embedding=embeddings
    )
    db.save_local("./faiss-db")