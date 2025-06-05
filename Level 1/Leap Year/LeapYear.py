while True:
    print("Leap Year Checker")
    answer = int(input("Input a year(Type -1 to quit):"))

    if answer % 4 == 0:
        print("Yes, it is a leap year.")
    elif answer % 400 == 0:
        print("Yes, it is a leap year.")
    elif answer == -1:
        break
    else:
        print("No, it is not a leap year.")
