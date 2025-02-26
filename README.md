# Command-Line ChatGPT Interface

**Project Description**:
   - Welcome to the Command Line ChatGPT Interface! This project allows you to have interactive conversations with ChatGPT through the command line.

1. **Installation**:
   - To get started with the ChatGPT interface, follow these simple steps to install the required dependencies and set up the environment.
   - 1. Create an OpenAI API Key.
        - Instructions can be found [here](https://platform.openai.com/docs/quickstart) or at https://platform.openai.com/docs/quickstart.
   - 2. Add API Key to your environment.
        - Instructions can also be found [here](https://platform.openai.com/docs/quickstart#create-and-export-an-api-key) or at https://platform.openai.com/docs/quickstart#create-and-export-an-api-key.
   - 3. Create a python virtual environment.
        - Create an environment by running ```python -m venv path/to/venv/```
        - For example, ```python -m venv .venv``` would create an environment named '.venv'.
   - 4. Activate virtual environment.
        - Activate the environment by running ```source path/to/venv/bin/activate```
        - For example, ```source .venv/bin/activate``` would activate the environment.
   - 5. Add OpenAI to environment.
        - With the virtual environment active, run ```pip install openai``` to install the OpenAI SDK to the environment.

2. **Usage**:
   - With the required dependencies installed and the virtual environment active, you can now run the command line chatgpt interface.
   - Simply run ```python3 chat_client.py``` to start chatting with chatgpt!
   - Type ```quit``` or ```exit``` to stop chatting. 
