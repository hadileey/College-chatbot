import json

def load_intents():
    with open("intents.json") as file:
        return json.load(file)

def find_response(user_input, intents):
    user_input = user_input.lower()

    for intent in intents["intents"]:
        for pattern in intent["patterns"]:
            if pattern in user_input:
                return intent["response"]

    return "Sorry, I don't understand your question."