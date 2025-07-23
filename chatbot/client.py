import os
from dotenv import load_dotenv, find_dotenv
from openai import AzureOpenAI

class AzureClient:
    def __init__(self):
        # Get environment variables
        load_dotenv(find_dotenv())
        self.api_version = os.getenv('API_VERSION')
        self.azure_endpoint = os.getenv('AZURE_ENDPOINT')
        self.api_key = os.getenv('API_KEY')
        
        # Validate required environment variables
        if not all([self.api_version, self.azure_endpoint, self.api_key]):
            raise ValueError(
                    """
                    Missing environment variables.
                    Please load all the required environment variables in the .env file:
                    API_VERSION, AZURE_ENDPOINT, API_KEY
                    """
            )
          
        # Initialize Azure OpenAI client
        self.client = AzureOpenAI(
            api_version=self.api_version,
            azure_endpoint=self.azure_endpoint,
            api_key=self.api_key,
        )