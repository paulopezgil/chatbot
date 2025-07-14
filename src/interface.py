from chatbot import ChatBot
from openai import AzureOpenAI
from dotenv import load_dotenv, find_dotenv
import panel as pn
import os

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

class Interface:
    def __init__(self, context: str = "", temperature: float = 0):
        # Initialize the Azure client
        self.azure_client = AzureClient()

        # Load the model name from environment variables
        load_dotenv(find_dotenv())
        self.model = os.getenv('MODEL')
        if not self.model:
            raise ValueError(
                        """
                        Missing MODEL environment variable.
                        Please set the MODEL variable in your .env file.
                        """
                  )
        
        # Create a ChatBot instance with the Azure client
        self.chatbot = ChatBot(self.azure_client.client, self.model, context, temperature)

        # Create a Panel interface for the chatbot
        self.chat_interface = pn.chat.ChatInterface(callback=self.chatbot.get_response)

        # Set up the Panel layout
        self.layout = pn.Column(
            pn.pane.Markdown("# Chatbot Interface"),
            self.chat_interface,
        )

    def serve(self, port: int = 8000):
        # Serve the Panel application
        self.layout.servable()
        pn.serve(self.layout, show=True, port=port)
        
