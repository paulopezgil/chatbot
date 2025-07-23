from dotenv import load_dotenv, find_dotenv
import os
from langchain_openai import AzureOpenAIEmbeddings

def embeddings():
    load_dotenv(find_dotenv())
    model = os.getenv('EMBEDDINGS_MODEL_NAME')
    api_key = os.getenv('AZURE_OPENAI_API_KEY')
    api_version = os.getenv("AZURE_OPENAI_API_VERSION")
    azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
    azure_deployment = os.getenv("EMBEDDINGS_DEPLOYMENT")

    # Validate required environment variables
    if not all([model, api_key, api_version, azure_endpoint, azure_deployment]):
        raise ValueError(
            """
            Missing environment variables.
            Please load all the required environment variables in the .env file:
            EMBEDDINGS_MODEL_NAME, AZURE_OPENAI_API_KEY, AZURE_OPENAI_API_VERSION,
            AZURE_OPENAI_ENDPOINT, EMBEDDINGS_DEPLOYMENT
            """
        )
    
    # Initialize and return an Azure OpenAI embeddings client
    embeddings = AzureOpenAIEmbeddings(
        model = model,
        api_key = api_key,
        api_version = api_version,
        azure_endpoint = azure_endpoint,
        azure_deployment = azure_deployment,
    )
    return embeddings