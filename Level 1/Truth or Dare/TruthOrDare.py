import random

truth = [
    "What's the most embarrassing thing you've ever done?",
    "Have you ever lied to get out of trouble?",
    "What’s a secret you’ve never told anyone?",
    "Who was your first crush?",
    "Have you ever cheated on a test?",
    "What’s something you’re afraid of?",
    "What's the weirdest dream you've ever had?",
    "Have you ever had a crush on a teacher?",
    "If you could be invisible for a day, what would you do?",
    "What's the biggest lie you've ever told your parents?"
]

dare = [
    "Do your best impression of someone in the room.",
    "Try to lick your elbow.",
    "Sing the chorus of your favorite song loudly.",
    "Do 10 jumping jacks.",
    "Speak in an accent for the next 5 minutes.",
    "Text someone random 'I know your secret...'",
    "Do a silly dance for 30 seconds.",
    "Eat a spoonful of mustard or another strong condiment.",
    "Try to touch your toes for 20 seconds.",
    "Act like a cat for the next 2 minutes."
]

while True:
    user = input("Enter 'T' for truth or 'D' for dare: ")
    if user.lower() == "quit":
        break
    elif user.lower() == "t":
        print("Truth:",random.choice(truth))
    elif user.lower() == "d":
        print("Dare:",random.choice(dare))
    else:
        print("Sorry, I didn't understand that.")