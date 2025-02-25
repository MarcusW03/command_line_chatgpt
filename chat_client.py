from openai import OpenAI
import os

class ChatClient():

    def __init__(self, api_key):
    
        self.client = OpenAI(api_key=api_key)

        self.model = "gpt-3.5-turbo"
    
    def get_client(self):
        return self.client
    
    def get_model(self):
        return self.model

#content_mod = "You are a helpful assistant, answering questions only about financial advise or credit card information. Respond thoughtfully and with plenty of information. For all other questions that are out of the scope of these two sectors, please respond politely that the question is out of your scope. In this case, do not answer it. Here is the question: "
content_mod = "You are a helpful assistant, helping a user as a simple command line interface. Please reply with simple text."
API_KEY = os.getenv("OPENAI_API_KEY")

def chatbot():

    try:
        chat_client = ChatClient(API_KEY)
    except Exception as e:
        print("Chat Features are currently unavailable")
        return

    client = chat_client.get_client()
    ai_model = chat_client.get_model()

    chat = [{"role": "developer", "content": content_mod},]

    print("Command Line Interface for ChatGPT")
    print("  Please type 'quit' or 'exit' to quit\n")
    
    # Accept user input
    prompt = input(">> How can I help?\n >> ")

    while prompt != "quit" and prompt != "exit":
        
        if prompt == "print_chat":
            print(chat)
            prompt = input(" >> ")
            continue

        chat.append({"role": "user", "content": prompt})

        try:
            completion = client.chat.completions.create(
                model=ai_model,
                messages=[
                    {"role": m["role"], "content": m["content"]}
                    for m in chat
                ],
                stream=False,
            )
            response = completion.choices[0].message.content
            print()
            print(response)
            print()
            chat.append({"role": "assistant", "content": response})
        except Exception as e:
            print("Whoops, there seems to be an error with the chatbot\n\n" + str(e))

        prompt = input(" >> ")

    del chat_client
    del chat
    del client
    print("\nThanks for chatting! Goodbye!")

if __name__ == "__main__":
    chatbot()