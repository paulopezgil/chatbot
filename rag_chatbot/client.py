import os
from dotenv import load_dotenv, find_dotenv
from openai import AzureOpenAI

def get_client():
    # Get environment variables
    load_dotenv(find_dotenv())
    api_version = os.getenv('API_VERSION')
    azure_endpoint = os.getenv('AZURE_ENDPOINT')
    api_key = os.getenv('API_KEY')
    
    # Validate required environment variables
    if not all([api_version, azure_endpoint, api_key]):
        raise ValueError(
                """
                Missing environment variables.
                Please load all the required environment variables in the .env file:
                API_VERSION, AZURE_ENDPOINT, API_KEY
                """
        )
        
    # Initialize and return an Azure OpenAI client
    client = AzureOpenAI(
        api_version=api_version,
        azure_endpoint=azure_endpoint,
        api_key=api_key,
        )
    return client