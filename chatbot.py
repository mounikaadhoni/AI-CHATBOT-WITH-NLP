import nltk
import random
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()
intents = {
    "greet": {
        "patterns": ["hi", "hello", "hey", "good morning", "good evening"],
        "responses": ["Hello!", "Hi there!", "Hey! How can I help you?"]
    },
    "goodbye": {
        "patterns": ["bye", "exit", "quit", "see you"],
        "responses": ["Goodbye!", "Bye! Have a nice day!", "See you soon!"]
    },
    "thanks": {
        "patterns": ["thanks", "thank you"],
        "responses": ["You're welcome!", "Happy to help!", "No problem!"]
    },
    "name": {
        "patterns": ["your name", "who are you"],
        "responses": ["I am an AI chatbot built using NLP.", "You can call me NLP Bot."]
    }
}

def chatbot_response(user_input):
    tokens = word_tokenize(user_input.lower())
    tokens = [lemmatizer.lemmatize(word) for word in tokens]

    for intent in intents.values():
        for pattern in intent["patterns"]:
            pattern_tokens = word_tokenize(pattern)
            if any(word in tokens for word in pattern_tokens):
                return random.choice(intent["responses"])

    return "Sorry, I didn't understand that."

print("Chatbot: Hello! Type 'bye' to exit.")

while True:
    user_input = input("You: ")

    if user_input.lower() in ["bye", "exit", "quit"]:
        print("Chatbot: Goodbye!")
        break

    response = chatbot_response(user_input)
    print("Chatbot:", response)