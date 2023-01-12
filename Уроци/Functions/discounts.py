def discount_choice(points):
    print("Your discount:")
    if 0 < points < 50:
        print("10% discount")
    elif 50 <= points < 100:
        print("15% discount")
    elif points >= 100:
        print("20% discount")
    else:
        print("Incorrect entry!")


points = int(input("Points earned: "))
discount_choice(points)

