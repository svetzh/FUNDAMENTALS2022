for cycle in range(5):
    month = input("Please insert a month in digits: ")
    year = input("Please insert a year: ")

    if month == "7":
        if year == "2007":
            print("You win!")
            break
        else:
            print("You guessed the month.")
    else:
        if year == "2007":
            print("You guessed the year.")
        else:
            print("Incorrect month and year.")

