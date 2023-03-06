coins = 100
print(f"Your coins are {coins}")

choice = input("Insert a number from 1 - store, 2 - watch an ad (+5), 3 - exit: ")

while choice != "3":
    if choice == "1":
        choice2 = input("Choose between 1 - sticker = 50 or 2 - t-shirt = 100 ")
        if choice2 == "1":
            coins -= 50
        elif choice2 == "2":
            coins -= 100
        else:
            print("Invalid choice")
    elif choice == "2":
        coins += 5
    else:
        print("Invalid choice")
    print(f"Your coins: {coins}")
    choice = input("Insert a number from 1 - store, 2 - watch an ad (+5), 3 - exit: ")