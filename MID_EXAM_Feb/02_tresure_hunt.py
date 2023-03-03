chest = input().split("|")
empty_list = []
command = input()
while command != "Yohoho!":
    action_args = command.split()
    action = action_args[0]

    if action == "Loot":
        items = action_args[1:]
        for item in items:
            if item not in chest:
                chest.insert(0, item)

    elif action == "Drop":
        index = int(action_args[1])
        if index not in range(0, len(chest)):
            command = input()
            continue
        else:
            removed_item = chest.pop(index)
            chest.append(removed_item)

    elif action == "Steal":
        count = int(action_args[1])
        removed_items = chest[-count:]
        print(", ".join(removed_items))
        chest = chest[:-count]

    command = input()

length_of_chest = len(chest)

if length_of_chest == 0:
    print("Failed treasure hunt. ")
else:
    suma = 0
    for el in chest:
        suma += len(el)
        # takes length of each element from each string in the list and sums it up
    average_gain = suma / length_of_chest
    print(f"Average treasure gain: {average_gain:.2f} pirate credits.")