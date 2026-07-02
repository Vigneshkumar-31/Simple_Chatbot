"""
Simple Rule-Based Chatbot
--------------------------
A beginner-friendly chatbot that responds based on keyword matching.
No ML/AI involved — just pattern matching and predefined rules.
"""

import random
import re

# Rules: each entry has a list of patterns (regex) and possible responses
rules = [
    {
        "patterns": [r"hi", r"hello", r"hey"],
        "responses": ["Hello! How can I help you today?", "Hi there!", "Hey! What's up?"]
    },
    {
        "patterns": [r"how are you"],
        "responses": ["I'm just a bunch of if-statements, but I'm doing great!", "Feeling good, thanks for asking!"]
    },
    {
        "patterns": [r"your name"],
        "responses": ["I'm ChatBot, your friendly rule-based assistant.", "You can call me ChatBot."]
    },
    {
        "patterns": [r"weather"],
        "responses": ["I can't check real weather yet, but I hope it's sunny where you are!"]
    },
    {
        "patterns": [r"bye", r"goodbye", r"see you"],
        "responses": ["Goodbye! Have a great day!", "See you later!", "Bye! Take care."]
    },
    {
        "patterns": [r"thank"],
        "responses": ["You're welcome!", "Anytime!", "Glad I could help!"]
    },
]

# Fallback responses when nothing matches
fallback_responses = [
    "I'm not sure I understand. Could you rephrase that?",
    "Hmm, I don't have a response for that yet.",
    "Can you say that differently?",
]


def get_response(user_input: str) -> str:
    user_input = user_input.lower().strip()

    for rule in rules:
        for pattern in rule["patterns"]:
            if re.search(pattern, user_input):
                return random.choice(rule["responses"])

    return random.choice(fallback_responses)


def chat():
    print("ChatBot: Hi! I'm a simple rule-based chatbot. Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ")

        if re.search(r"bye|goodbye|exit|quit", user_input.lower()):
            print("ChatBot:", random.choice(rules[4]["responses"]))
            break

        response = get_response(user_input)
        print("ChatBot:", response)


if __name__ == "__main__":
    chat()