quantity_food_gr = float(input()) * 1000
quantity_hay_gr = float(input()) * 1000
quantity_cover_gr = float(input()) * 1000
month = 30

guinea_eats_food = 300
guinea_weight_gr = float(input()) * 1000

for day in range(1, month + 1):

    quantity_food_gr -= guinea_eats_food
    if day % 2 == 0:
        quantity_hay_gr -= (quantity_food_gr * .05)
    if day % 3 == 0:
        quantity_cover_gr -= guinea_weight_gr / 3

food_kg = (quantity_food_gr / 1000)
hay_kg = (quantity_hay_gr / 1000)
cover_kg = (quantity_cover_gr / 1000)

if food_kg <= 0 or hay_kg <= 0 or cover_kg <= 0:
    print("Merry must go to the pet store!")
else:
    print(f"Everything is fine! Puppy is happy! Food:"
          f" {food_kg:.2f}, "
          f"Hay: {hay_kg:.2f}, "
          f"Cover: {cover_kg:.2f}.")
