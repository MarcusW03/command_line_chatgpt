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
        - Additional information on creating and using virtual environments can be found [here](https://docs.python.org/3/library/venv.html#creating-virtual-environments). 

2. **Usage**:
   - With the required dependencies installed and the virtual environment active, you can now run the command line chatgpt interface.
   - Simply run ```python3 chat_client.py``` to start chatting with chatgpt!
   - Type ```quit``` or ```exit``` to stop chatting.

3. **Advanced Usage**:
   - Add the command line chatgpt as an alias in your terminal!
   - In the same way you added the api key to your environment in 1b, create an alias in your environment for the command line chatgpt.
   - In your .zshrc or .bashrc file, add ```alias chat="python3 $HOME/path/to/your/file/chat_client.py"``` where /path/to/your/file is the path needed to your file from your home directory.
   - For example, ```alias chat="python3 $HOME/command_line_chat/chat_client.py``` would work if chat_client.py was stored in a directory inside of your home directory.
   - For this to run properly, make sure your environment is active!
     - For an even more advanced usage, create a bash script that activates the environment and then runs chat_client.py.
     - Then, you would run the bash script as your alias. For example, ```alias chat="sh $HOME/command_line_chat/chat.sh``` where chat.sh runs ```source /path/to/venv/bin/activate``` and then ```python3 $HOME/path/to/your/file/chat_client.py```
  
4. **Demo**:
   - ![command line chatgpt demo](cmline_demo.gif)
