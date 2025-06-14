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
            player_cards.append(random.randint(1,13))
        dealer_cards.append(random.randint(1,13))
        game_over = False

        while True:

            player_display = []
            for card in player_cards:
                if card == 1:
                    name = "A"
                elif card == 11:
                    name = "J"
                elif card == 12:
                    name = "Q"
                elif card == 13:
                    name = "K"
                else:
                    name = str(card)


                suit_num = random.randint(0, 3)
                if suit_num == 0:
                    suit = "♠"
                elif suit_num == 1:
                    suit = "♥"
                elif suit_num == 2:
                    suit = "♦"
                else:
                    suit = "♣"

                player_display.append(name + suit)

            print("Player cards:", player_display)


            player_total = 0
            for card in player_cards:
                if card >= 11:
                    player_total = player_total + 10
                else:
                    player_total = player_total + card

            if player_total == 21:
                print("Player has a Baby Blackjack!")
                break
            elif player_cards == [1, 1, 1, 1]:
                print("Natural! You win!")
                purse = purse + bet + (bet*(7/5))
                game_over = True
                break
            elif player_total > 21:
                print("You lost")
                game_over = True
                purse = purse - bet
                break
            decision = input("Would you like to (h)hit or (s)stand?\n: ")

            if decision == "h":
                player_cards.append(random.randint(1,13))
            elif decision == "s":
                print("You chose to stand")
                break

        if not game_over:
            while True:
                dealer_cards.append(random.randint(1,13))


                dealer_display = []
                for card in dealer_cards:
                    if card == 1:
                        name = "A"
                    elif card == 11:
                        name = "J"
                    elif card == 12:
                        name = "Q"
                    elif card == 13:
                        name = "K"
                    else:
                        name = str(card)


                    suit_num = random.randint(0, 3)
                    if suit_num == 0:
                        suit = "♠"
                    elif suit_num == 1:
                        suit = "♥"
                    elif suit_num == 2:
                        suit = "♦"
                    else:
                        suit = "♣"

                    dealer_display.append(name + suit)

                print("Dealer cards:", dealer_display)


                dealer_total = 0
                for card in dealer_cards:
                    if card >= 11:
                        dealer_total = dealer_total + 10
                    else:
                        dealer_total = dealer_total + card
                if dealer_total > 21:
                    print("Player Won")
                    purse = purse + bet
                    break
                if  dealer_total > player_total:
                    print("Dealer Won")
                    purse = purse - bet
                    break
                if dealer_total == 21:
                    if player_total == 21:
                        print("Tie")
                        break
                    elif player_total < 21:
                        print("Dealer Won")
                        purse = purse - bet
                        break


print("Thanks for your money")