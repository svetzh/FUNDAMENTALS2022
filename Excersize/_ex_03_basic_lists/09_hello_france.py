items = input().split("|")
budget = int(input())

profit = 0
new_item_prices = []
data_prices = []
condition = False

for item in items:
    item_info = item.split("->")
    item_type = item_info[0]
    item_price = float(item_info[1])
    condition = False

    if item_type == "Clothes":
        if item_price <= 50.00:
            condition = True
    elif item_type == "Shoes":
        if item_price <= 35.00:
            condition = True

    elif item_type == "Accessories":
        if item_price <= 20.5:
            condition = True
    if condition:
        if budget >= item_price:
            budget -= item_price
            profit += item_price * .4
            new_price = item_price + (item_price * 0.40)
            new_item_prices.append(new_price)
            data_prices.append(f"{new_price:.2f}")
print(" ".join(data_prices))
print(f"Profit: {profit:.2f}")

total_sum = budget + sum(new_item_prices)
if total_sum >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")
