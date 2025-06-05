import random

purse = 20

while purse > 0:
    print("You have", purse, "Euro.")
    bet = int(input("How much would you like to bet?\n: "))
    if bet > purse:
        print("Sorry, but you don't have enough money.")
    else:
        player_cards = []
        dealer_cards = []


        for i in range(2):
            player_cards.append(random.randint(1,2))
            dealer_cards.append(random.randint(1,2))
        game_over = False
        while True:
            print("Player cards:", player_cards)
            decision = input("Would you like to (h)hit or (s)stand?\n: ")

            if decision == "h":
                player_cards.append(random.randint(1,2))
            elif decision == "s":
                print("You chose to stand")
                break
            if sum(player_cards) == 5:
                print(player_cards)
                print("Player has a Baby Blackjack!")
                break
            elif player_cards == [1, 1, 1, 1]:
                print(player_cards)
                print("Natural! You win!")
                purse = purse + bet + (bet*(7/5))
                game_over = True
                break
            elif sum(player_cards) > 5:
                print(player_cards)
                print("You lost")
                game_over = True
                purse = purse - bet
                break

        if not game_over:
            print("Dealer cards:", dealer_cards)
            while True:
                dealer_cards.append(random.randint(1,2))
                print("Dealer cards:", dealer_cards)
                if sum(dealer_cards) == 5:
                    if sum(player_cards )== 5:
                        print("Tie")
                        break
                    elif sum(player_cards) < 5:
                        print("Dealer Won")
                        purse = purse - bet
                        break
                elif sum(dealer_cards) > 5:
                    print("Player Won")
                    purse = purse + bet
                    break

print("Thanks for your money")
