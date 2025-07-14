from interface import Interface

if __name__ == "__main__":
    # Set up the context for the chatbot
    context = """
        You are a helpful assistant.
        Answer the user's questions to the best of your ability.
        Try to be concise and clear.
    """

    # Create an instance of the Interface class
    interface = Interface(context = context, temperature = 0.5)

    # Serve the interface on port 8000
    interface.serve(port=8000)