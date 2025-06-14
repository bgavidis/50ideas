user = False
while not user:

    user_selection = input("What would you like to convert?\n"
                         "1)Lengths\n"
                         "2)Weights/Mass\n"
                         "3)Volume\n"
                         "4)Temperature\n"
                         "5)Area\n"
                         "6)Speed\n"
                         "q)To quit\n:"
                        )

    if user_selection == "1":
        user_selection_2 = input("What would you like to convert to?(example:feet to meters\n"
                         "1)Feet -> Meters\n"   
                         "2)Meters -> Feet\n"
                         "3)Inches -> Centimeters\n"
                         "4)Centimeters -> Inches \n"
                         "5)Miles -> Kilometers\n"
                         "6)Kilometers -> Miles\n:"
                         )
        if user_selection_2 == "1":
            user_input = float(input("Enter the length in feet\n: "))
            result = user_input * 0.3048
            print(f"{user_input} feet is {result} meters")
        elif user_selection_2 == "2":
            user_input = float(input("Enter the length in meters\n: "))
            result = user_input / 0.3048
            print(f"{user_input} meters is {result} feet")
        elif user_selection_2 == "3":
            user_input = float(input("Enter the length in inches\n: "))
            result = user_input * 2.54
            print(f"{user_input} inches is {result} centimeters")
        elif user_selection_2 == "4":
            user_input = float(input("Enter the length in centimeters\n: "))
            result = user_input / 2.54
            print(f"{user_input} centimeters is {result} inches")
        elif user_selection_2 == "5":
            user_input = float(input("Enter the length in miles\n: "))
            result = user_input * 1.609344
            print(f"{user_input} miles is {result} kilometers")
        elif user_selection_2 == "6":
            user_input = float(input("Enter the length in kilometers\n: "))
            result = user_input / 1.609344
            print(f"{user_input} kilometers is {result} miles")
        else:
           print("Invalid input")
    if user_selection == "2":
        user_input = input("Enter what you want to convert:\n"
                           "1)pounds to kilograms\n"
                           "2)kilograms to pounds")
        if user_input == "1":
            user_input = float(input("Enter the weight in pounds\n: "))
            result = user_input * 0.453592
            print(f"{user_input} pounds is {result} kilograms")
        elif user_input == "2":
            user_input = float(input("Enter the weight in kilograms\n: "))
            result = user_input / 0.453592
            print(f"{user_input} kilograms is {result} pounds")
        else:
           print("Invalid input")
    if user_selection == "3":
        user_input = input("Enter what you want to convert:\n"
                           "1)cubic feet to cubic meters\n"
                           "2)cubic meters to cubic feet\n:")
        if user_input == "1":
            user_input = float(input("Enter the volume in cubic feet\n: "))
            result = user_input * 0.0283168
            print(f"{user_input} cubic feet is {result} cubic meters")
        elif user_input == "2":
            user_input = float(input("Enter the volume in cubic meters\n: "))
            result = user_input / 0.0283168
            print(f"{user_input} cubic meters is {result} cubic feet")
        else:
           print("Invalid input")
    if user_selection == "4":
        user_input = input("Enter what you want to convert:\n"
                           "1)degrees celsius to degrees fahrenheit\n"
                           "2)degrees fahrenheit to degrees celsius\n:")
        if user_input == "1":
            user_input = float(input("Enter the temperature in degrees celsius\n: "))
            result = (user_input * 9 / 5) + 32
            print(f"{user_input} degrees celsius is {result} degrees fahrenheit")
        elif user_input == "2":
            user_input = float(input("Enter the temperature in degrees fahrenheit\n: "))
            result = (user_input - 32) * 5 / 9
            print(f"{user_input} degrees fahrenheit is {result} degrees celsius")
        else:
            print("Invalid input")
    if user_selection == "5":
        user_input = input("Enter what you want to convert:\n"
                           "1)square feet to square meters\n"
                           "2)square meters to square feet\n:")
        if user_input == "1":
            user_input = float(input("Enter the area in square feet\n: "))
            result = user_input * 0.092903
            print(f"{user_input} square feet is {result} square meters")
        elif user_input == "2":
            user_input = float(input("Enter the area in square meters\n: "))
            result = user_input / 0.092903
            print(f"{user_input} square meters is {result} square feet")
        else:
            print("Invalid input")
    if user_selection == "6":
        user_input = input("Enter what you want to convert:\n"
                           "1)miles per hour to kilometers per hour\n"
                           "2)kilometers per hour to miles per hour\n:")
        if user_input == "1":
            user_input = float(input("Enter the speed in miles per hour\n: "))
            result = user_input * 0.44704
            print(f"{user_input} miles per hour is {result} kilometers per hour")
        elif user_input == "2":
            user_input = float(input("Enter the speed in kilometers per hour\n: "))
            result = user_input / 0.44704
            print(f"{user_input} kilometers per hour is {result} miles per hour")
        else:
            print("Invalid input")
    elif user_selection == "q":
        user = True
    else:
        print("Invalid input")





    