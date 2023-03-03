products = input().split()
bakery = {}
for el in range(0, len(products), 2):
    product = products[el]
    quantity = products[el + 1]
    bakery[product] = int(quantity)

searched_products = input().split()
for p in searched_products:
    if p in bakery:
        print(f"We have {bakery[p]} of {p} left")
    else:
        print(f"Sorry, we don't have {p}")

