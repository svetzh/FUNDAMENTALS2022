vehicles = input().split(">>")
tax = 0
counter = 0
for car in vehicles:
    car = car.split()
    type_car = car[0]
    years = int(car[1])
    run_kms = int(car[2])

    if type_car == "family":
        initial_tax = 50
        tax = (run_kms // 3000 * 12) + initial_tax - years * 5
        counter += tax
        print(f"A {type_car} car will pay {tax:.2f} euros in taxes.")
    elif type_car == "heavyDuty":
        initial_tax = 80
        tax = (run_kms // 9000 * 14) + initial_tax - years * 8
        counter += tax
        print(f"A {type_car} car will pay {tax:.2f} euros in taxes.")
    elif type_car == "sports":
        initial_tax = 100
        tax = (run_kms // 2000 * 18) + initial_tax - years * 9
        counter += tax
        print(f"A {type_car} car will pay {tax:.2f} euros in taxes.")
    else:
        print("Invalid car type.")

print(f"The National Revenue Agency will collect {counter:.2f} euros in taxes.")
