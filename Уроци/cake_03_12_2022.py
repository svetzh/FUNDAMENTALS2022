weight = int(input("What is the weight of the cake? "))
filling = input("Enter filling: ")

if weight <= 2500:
    price = 3000
else:
    price = 5000

if filling == "fruit":
    price += 1000
else:
    price += 500

print(price)
