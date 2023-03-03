days = int(input())
dayly_plunder = int(input())
expected_plunder = float(input())

sum_plunder = 0
third_day_bonus = dayly_plunder * .5

for day in range(1, days + 1):
    sum_plunder += dayly_plunder
    if day % 3 == 0:
        sum_plunder += third_day_bonus

    if day % 5 == 0:
        sum_plunder *= .7


if sum_plunder >= expected_plunder:
    print(f"Ahoy! {sum_plunder:.2f} plunder gained.")
elif sum_plunder < expected_plunder:
    percentage = sum_plunder / expected_plunder * 100
    print(f"Collected only {percentage:.2f}% of the plunder.")
