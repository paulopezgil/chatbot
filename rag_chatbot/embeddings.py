from dotenv import load_dotenv, find_dotenv
import os
from langchain_openai import AzureOpenAIEmbeddings

def get_embeddings():
    load_dotenv(find_dotenv())
    azure_deployment = os.getenv("AZURE_DEPLOYMENT_EMBEDDINGS")
    openai_api_version=os.getenv("API_VERSION")

    # Validate required environment variables
    if not all([azure_deployment, openai_api_version]):
        raise ValueError(
            """
            Missing environment variables.
            Please load all the required environment variables in the .env file:
            AZURE_DEPLOYMENT_EMBEDDINGS, AZURE_OPENAI_API_VERSION
            """
        )
    
    # Initialize and return an Azure OpenAI embeddings client
    embeddings = AzureOpenAIEmbeddings(
        azure_deployment=azure_deployment,
        openai_api_version=openai_api_version,
    )
    return embeddings