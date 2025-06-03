
q1 = input("Who is Tata Simonyan?\n1)Football player\n2)Musician\n3)Actor\n4)Model")
if q1 == "Musician":
    print("Bravo he is a famous musician\nNext question:")
    q2 = input("Which country is the biggest in population?\n1)India\n2)China\n3)USA\n4)Russia")
    if q2 == "India":
        print("Bravo yes its India\nNext question:")
        q3 = input("Who is the first person you should call after getting a promotion?\n1)Tata Simonyan\n2)Your Girlfriend\n3)Your Brother\n4)Your Father")
        if q3 == "Your Girlfriend":
            print("Congratulation you won 1million dollars!")
        else:
            print("Sorry you lost!\nYou were so close!")
    else:
        print("Sorry you lost!")
else:
    print("Sorry you lost!")