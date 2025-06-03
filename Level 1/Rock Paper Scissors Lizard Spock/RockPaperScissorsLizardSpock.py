import random

hand = ["rock","paper","scissors","lizard","spock"]

opponent = random.choice(hand)

you = input("Rock, Paper, Scissors, Lizard, Spock: ")

print("Opponent chose: ",opponent)

if you == opponent:
    print("Tie!")
elif you == "rock":
    if opponent == "scissors":
        print("You Win")
    elif opponent == "lizard":
        print("You Win")
    else:
        print("You Lose")
elif you == "paper":
    if opponent == "rock":
        print("You Win")
    elif opponent == "spock":
        print("You Win")
    else:
        print("You Lose")
elif you == "scissors":
    if opponent == "paper":
        print("You Win")
    elif opponent == "lizard":
        print("You Win")
    else:
        print("You Lose")
elif you == "lizard":
    if opponent == "spock":
        print("You Win")
    elif opponent == "paper":
        print("You Win")
    else:
        print("You Lose")
elif you == "spock":
    if opponent == "rock":
        print("You Win")
    elif opponent == "scissors":
        print("You Win")
    else:
        print("You Lose")

