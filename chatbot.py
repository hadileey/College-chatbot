from utils import load_intents, find_response

def chatbot():
    print("===== College Chatbot =====")
    print("Type 'exit' to quit\n")

    intents = load_intents()

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Bot: Goodbye!")
            break

        response = find_response(user_input, intents)
        print("Bot:", response)

if __name__ == "__main__":
    chatbot()