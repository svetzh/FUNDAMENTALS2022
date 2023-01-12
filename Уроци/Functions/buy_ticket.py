def ticket(price):
    insurance = input("Insurance: ")
    meals = input("Meals: ")
    if insurance == "yes":
        price += 20
    if meals == "yes":
        price += 50
    return price

price = 100
print(f"Total price: {ticket(price)}")
