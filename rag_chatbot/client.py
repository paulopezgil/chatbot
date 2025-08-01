import os
from dotenv import load_dotenv, find_dotenv
from langchain_openai import AzureChatOpenAI

def client():
    # Get environment variables
    load_dotenv(find_dotenv())
    api_version = os.getenv('AZURE_OPENAI_API_VERSION')
    azure_endpoint = os.getenv('AZURE_OPENAI_ENDPOINT')
    api_key = os.getenv('AZURE_OPENAI_API_KEY')
    
    # Validate required environment variables
    if not all([api_version, azure_endpoint, api_key]):
        raise ValueError(
            """
            Missing environment variables.
            Please load all the required environment variables in the .env file:
            AZURE_OPENAI_API_VERSION, AZURE_OPENAI_ENDPOINT, AZURE_OPENAI_API_KEY
            """
        )
        
    # Initialize and return an Azure OpenAI client
    client = AzureChatOpenAI(
        azure_deployment = os.getenv('GPT_MODEL'),
        api_version=api_version,
        azure_endpoint=azure_endpoint,
        api_key=api_key,
    )
    return client