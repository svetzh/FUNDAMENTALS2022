products = {}
raw_data = input()
while raw_data != 'buy':
    line = raw_data.split()
    product_name = line[0]
    price = float(line[1])
    quantity = int(line[2])

    if product_name not in products:
        products[product_name] = [price, quantity]
    else:
        products[product_name] = [price, (quantity + products[product_name][1])]

    raw_data = input()

for i in products:
    total_price = products[i][0] * products[i][1]
    print(f"{i} -> {total_price:.2f}")
