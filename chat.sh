eval "$(conda shell.bash hook)"

conda activate owlhacks

python3 $HOME/chatgpt_command_line/chat_client.py

conda deactivate