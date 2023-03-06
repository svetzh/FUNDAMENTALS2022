num_of_orders = int(input())
total_price = 0.0
current_price = 0

for i in range(num_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    daily_capsules_needed = int(input())
    if price_per_capsule < 0.01 or price_per_capsule > 100:
        continue
    elif days < 1 or days > 31:
        continue
    elif daily_capsules_needed < 1 or daily_capsules_needed > 2000:
        continue

    price = price_per_capsule * days * daily_capsules_needed
    current_price += price
    print(f"The price for the coffee is: ${price:.2f}")

print(f'Total: ${current_price:.2f}')
