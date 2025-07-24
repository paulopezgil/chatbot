## 1. Description of the project

In this project, a GUI for a chatbot is developed using the Azure OpenAI API for python all together with the panel library.

## 2. Setup

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
1. **Deploy an Azure OpenAI resource**

    Use the following link: https://ai.azure.com/
2. **Save the details to the .env file:**
    ```bash
    echo API_VERSION=\"your-version-here\" >> .env
    echo AZURE_ENDPOINT=\"your-endpoint-here\" >> .env
    echo API_KEY=\"your-api-key-here\" >> .env
    echo MODEL=\"your-model-here\" >> .env
    ```