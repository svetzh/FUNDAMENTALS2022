groceries = input().split('!')

raw_input = input()
while raw_input != "Go Shopping!":
    command = raw_input.split()

    action = command[0]
    item = command[1]
    if action == "Urgent":
        if item in groceries:
            raw_input = input()
            continue
        groceries.insert(0, item)
    elif action == "Unnecessary":
        if item in groceries:
            groceries.remove(item)
    elif action == "Correct":
        item2 = command[2]
        if item in groceries:
            for i in range(len(groceries)):
                if groceries[i] == item:
                    groceries[i] = item2
    elif action == "Rearrange":
        if item in groceries:
            groceries.remove(item)
            groceries.append(item)

    raw_input = input()
print(", ".join(groceries))

######################################################
#  https://pastebin.com/ZxzGYuLU
products = input().split('!')

while True:
    line = input()
    if line == "Go Shopping!":
        break

    command_args = line.split()
    command = command_args[0]
    product = command_args[1]

    if command == "Urgent":
        if product not in products:
            products.insert(0, product)
    elif command == "Unnecessary":
        if product in products:
            products.remove(product)
    elif command == "Correct":
        new_product = command_args[2]
        if product in products:
            idx = products.index(product)
            products[idx] = new_product
        if product in products:
            idx = products.index(product)
    elif command == "Rearrange":
        if product in products:
            # find current index of product in products
            idx = products.index(product)
            products.pop(idx)
            products.append(product)

print(', '.join(products))










