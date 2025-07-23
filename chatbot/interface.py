from chatbot import ChatBot
from client import AzureClient

from dotenv import load_dotenv, find_dotenv
import os
import panel as pn

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