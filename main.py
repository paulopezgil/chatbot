from chatbot import ChatBot
from openai import AzureOpenAI
import os
from dotenv import load_dotenv, find_dotenv
import panel as pn
pn.extension()

# Read local .env file
load_dotenv(find_dotenv())

# Initialize OpenAI client with environment variables
client = AzureOpenAI(
    api_version = os.getenv('API_VERSION'),
    azure_endpoint = os.getenv('AZURE_ENDPOINT'), # type: ignore
    api_key = os.getenv('API_KEY'),
)
model = os.getenv('MODEL')

# Create a ChatBot instance
chatbot = ChatBot(
    client = client,
    model = model,
    context = """
        You are a helpful assistant.
        You can answer questions and provide information based on the context provided.
    """
)

# Create a Panel interface for the chatbot
chat_interface = pn.chat.ChatInterface(callback=chatbot.get_response)

# Set up the Panel layout
layout = pn.Column(
    pn.pane.Markdown("# Chatbot Interface"),
    chat_interface,
)
layout.servable()

# Serve the Panel application
if __name__ == "__main__":
    pn.serve(layout, show=True, port=8000)
    
