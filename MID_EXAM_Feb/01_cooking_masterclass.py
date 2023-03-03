from math import ceil

budget = float(input())
students = int(input())

flour_package_price = float(input())
single_egg_price = float(input())
single_apron_price = float(input())

free_package = 0

for student in range(1, students + 1):
    if student % 5 == 0:
        free_package += 1

total_flour_package_price = flour_package_price * (students - free_package)
total_eggs_price = (single_egg_price * 10) * students
total_price_aprons = single_apron_price * ceil(students * 1.2)
total = total_price_aprons + total_eggs_price + total_flour_package_price
diff = abs(total-budget)
if total <= budget:
    print(f"Items purchased for {total:.2f}$.")
else:
    print(f"{diff:.2f}$ more needed.")
