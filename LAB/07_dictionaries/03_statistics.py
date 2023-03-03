input_command = input()
products = {}
while input_command != "statistics":

    input_args = input_command.split(":")
    p = input_args[0]
    q = int(input_args[1])

    if p not in products:
        products[p] = 0
    products[p] += q
    # if p in products:
    #     products[p] += q
    # else:
    #     products[p] = q

    input_command = input()

print("Products in stock:")
for k, v in products.items():
    print(f"- {k}: {v}")

print(f"Total Products: {len(products)}")
print(f"Total Quantity: {sum(products.values())}")