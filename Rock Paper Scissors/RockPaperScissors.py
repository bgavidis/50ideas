import random

hand = ["rock","paper","scissors"]

opponent = random.choice(hand)

you = input("Rock, Paper, Scissors: ")

if you == opponent:
    print("Tie!")
elif you == "rock":
    if opponent == "paper":
        print("You lose!")
    else:
        print("You win!")
elif you == "paper":
    if opponent == "scissors":
        print("You lose!")