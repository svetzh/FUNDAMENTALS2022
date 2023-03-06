lines = int(input())
capacity = 255

liters_of_water = 0
sum_liters = 0
overall_capacity = 0
for _ in range(lines):
    liters_of_water = int(input())
    if capacity - liters_of_water < 0:
        print("Insufficient capacity!")
        continue
    sum_liters += liters_of_water
    capacity -= liters_of_water
print(sum_liters)

