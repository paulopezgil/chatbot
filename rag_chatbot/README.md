# 1. Description of the project

In this project, a GUI for a chatbot is developed using the Azure OpenAI API for python all together with LangChain in order to implement a RAG system for uploading a PDF file.

# 2. Setup

## 2.1 Activate virtual environment

1. **Create a virtual environment:**
    ```bash
    python3 -m venv .venv
    ```

2. **Activate the environment:**
    ```bash
    source .venv/bin/activate
    ```

3. **Install the requirements:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Deactivate the environment:**
    ```bash
    deactivate
    ```

## 2.2 Activate an Azure OpenAI API Key
1. **Deploy an Azure OpenAI LLM resource and embedding resource**

    Use the following link: https://ai.azure.com/
2. **Save the details to the .env file:**
    ```bash
    echo AZURE_OPENAI_API_KEY=\"your-api-key-here\" >> .env
    echo AZURE_OPENAI_API_VERSION=\"your-version-here\" >> .env
    echo AZURE_OPENAI_ENDPOINT=\"your-endpoint-here\" >> .env
    echo GPT_MODEL=\"your-llm-model-here\" >> .env
    echo EMBEDDINGS_MODEL_NAME=\"your-embeddings-model-here\" >> .env
    echo EMBEDDINGS_DEPLOYMENT=\"your-embeddings-deployment-here\" >> .env
    ```

# 3. Project architecture

The hierarchy of the project scripts is as follows:

```
client      embeddings      text_splitter      document_loader
  │             │                │                   │
  │             │                │                   │
  │          database            │                   │
  │             │                │                   │
  │             │                │                   │
  │             └────────────────┴─┬─────────────────┘
  │                                │     
  │                                │ 
  │                                │
  │                                │
  │                            retriever
  │                                │
  │                                │
  └────────────────────────── retriever_qa
                                   │
                                   │
                                  main
```
The functions found in those scripts provide the following functionality:

- **client()**: Initializes and returns an Azure OpenAI chat client using environment variables for API configuration
- **embeddings()**: Creates and returns an Azure OpenAI embeddings client for converting text to vector representations
- **text_splitter(data)**: Splits documents into smaller chunks (1000 chars with 50 char overlap) for better processing
- **document_loader(file)**: Loads PDF documents using PyPDFLoader and returns the loaded document content
- **vector_database(chunks)**: Creates a Chroma vector database from document chunks using the embeddings model
- **retriever(file)**: Orchestrates the document processing pipeline: loads → splits → vectorizes → creates retriever object
- **retriever_qa(file, query)**: Main QA function that combines the LLM client with the retriever to answer questions based on uploaded documents
- **main**: Creates and launches a Gradio web interface for the RAG chatbot with file upload and query input capabilities