from retriever import retriever
from client import client
from langchain.chains import RetrievalQA

def retriever_qa(file, query):
    llm = client()
    retriever_obj = retriever(file)
    qa = RetrievalQA.from_chain_type(llm=llm, 
                                    chain_type="stuff", 
                                    retriever=retriever_obj, 
                                    return_source_documents=False)
    response = qa.invoke(query)
    return response['result']