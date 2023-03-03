fire_cells = input().split("#")
water_amount = int(input())
effort = 0
fire = 0
value_cells = []
for cell in fire_cells:
    cell = cell.split(" = ")
    type_of_fire = cell[0]
    fire_amount = int(cell[1])

    if type_of_fire == "High":
        if not 81 <= fire_amount <= 125:
            continue
    elif type_of_fire == "Medium":
        if not 51 <= fire_amount <= 80:
            continue
    elif type_of_fire == "Low":
        if not 1 <= fire_amount <= 50:
            continue
    if water_amount < fire_amount:
        continue

    value_cells.append(fire_amount)
    water_amount -= fire_amount

res = sum(value_cells)
effort = res * .25

print("Cells:")
for cell in value_cells:
    print(f" - {cell}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {res}")

