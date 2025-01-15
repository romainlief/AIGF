from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from GF_Tsundere import Tsundere
from GF_Yandere import Yandere

template = """
Answer the following question:

Here is the conservation history: {context}

Question: {question}

Answer: 
"""

model = OllamaLLM(model="llama3.2")
prompt = ChatPromptTemplate.from_template(template=template)
chain = prompt | model


def intro_print():
    print("Welcome to the AI Chatbot!")
    print("You can quit the chat by typing 'quit' or 'exit'.")
    print()


def print_choice_GF():
    print("Choose the girlfriend personality you want to talk to:")
    print("1. Shy")
    print("2. Tsundere")
    print("3. Normal")
    print()


def GF_choice():
    intro_print()
    context_jade = "You are my girlfriend Jade, answer my questions as Jade the girl who loves me, the assisant, only."
    print_choice_GF()
    choice = (input("Enter your choice: "))
    print()
    while choice not in {'1', '2', '3'}:
        print("Invalid choice. Please enter a valid choice.")
        print()
        choice = (input("Enter your choice: "))
        print()
    if choice == "1":
        print("You'll be talking to the shy girlfriend.")
        Yandere1 = Yandere("Yandere")
        return Yandere1.get_context()
    elif choice == "2":
        print("You'll be talking to the tsundere girlfriend.")
        Tsundere1 = Tsundere("Tsundere")
        return Tsundere1.get_context()
    elif choice == "3":
        print("You'll be talking to Jade the normal girlfriend.")
        return context_jade
    
    
def chat(context_choice):
    exit_commands = ["quit", "exit", "goodbye", "bye"]
    while user_input := input("You: "):
        if user_input in exit_commands:
            break
        result = chain.invoke({"context" : context_choice, "question" : user_input})
        print()
        print("AI: ", result)
        print()
        context_choice += f"\nUser: {user_input}\nAI: {result}"


if __name__ == "__main__":
    try:
        chat(context_choice=GF_choice())
    except KeyboardInterrupt as e:
        print(e)
    except Exception as e:
        print(e)
