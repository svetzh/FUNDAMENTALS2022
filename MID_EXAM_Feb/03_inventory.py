collecting_items = [x for x in input().split(", ")]

raw_command = input()
while raw_command != "Craft!":
    command = raw_command.split(" - ")
    action = command[0]
    the_item = command[1]
    if action == "Collect":
        if the_item not in collecting_items:
            collecting_items.append(the_item)
        else:
            raw_command = input()
            continue

    elif action == "Drop":
        if the_item in collecting_items:
            collecting_items.remove(the_item)
        else:
            raw_command = input()
            continue

    elif action == "Combine Items":
        split_item = the_item.split(":")
        old_item = split_item[0]
        new_item = split_item[1]
        if old_item in collecting_items:
            old_item = collecting_items.index(old_item)
            collecting_items.insert(old_item + 1, new_item)

    elif action == "Renew":
        if the_item in collecting_items:
            collecting_items.remove(the_item)
            collecting_items.append(the_item)

    raw_command = input()

print(", ".join(collecting_items))
