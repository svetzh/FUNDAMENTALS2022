phone_book = {}
n = 0
while True:
    line = input()
    parts = line.split("-")
    if len(parts) == 1:
        n = int(line)
        break

    name = parts[0]
    number = parts[1]
    phone_book[name] = number

for _ in range(n):
    name = input()
    if name in phone_book:
        print(f"{name} -> {phone_book[name]}")
    else:
        print(f"Contact {name} does not exist.")