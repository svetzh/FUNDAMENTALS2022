command = input().lower().split()
legend_items = {
    "shards": 0,
    "fragments": 0,
    "motes": 0
}

is_obtained = False

while not is_obtained:
    for idx in range(0, len(command), 2):
        key = command[idx + 1]
        value = int(command[idx])

        if key not in legend_items:
            legend_items[key] = 0
        legend_items[key] += value

        if legend_items["shards"] >= 250:
            print('Shadowmourne obtained!')
            legend_items["shards"] -= 250
            is_obtained = True
        elif legend_items["fragments"] >= 250:
            print('Valanyr obtained!')
            legend_items["fragments"] -= 250
            is_obtained = True
        elif legend_items["motes"] >= 250:
            print('Dragonwrath obtained!')
            legend_items["motes"] -= 250
            is_obtained = True

        if is_obtained:
            break
    if is_obtained:
        break

    command = input().lower().split()

for material, quantity in legend_items.items():
    print(f"{material}: {quantity}")

