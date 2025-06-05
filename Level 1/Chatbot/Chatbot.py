import time
import random

jokes = ["What is it called when a cat wins a dog show? A CAT-HAS-TROPHY", "Why don't cats like online shopping? They prefer a cat-alogue."]

while True:
    user = input("You:")
    if user.lower() == "quit":
        break
    elif user.lower() == "hello" or user.lower() == "hi":
        print("Chatbot: Hello, how can I help you?")
    elif user.lower() == "how are you":
        print("Chatbot: I am good, thank you.")
    elif user.lower() == "what time is it":
        print("Chatbot: The time is", time.ctime())
    elif user.lower() == "give me a number":
        print("Chatbot: The number I am thinking is", random.randint(1,10))
    elif user.lower() == "give me a joke":
        print("Chatbot:", random.choice(jokes))
    else:
        print("Chatbot: Sorry, I don't understand.")



