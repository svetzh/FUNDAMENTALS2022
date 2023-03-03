events = input().split("|")

energy = 100
coins = 100
gained_energy = 0
closed_condition = False

for event in events:
    event_info = event.split('-')

    event_type = event_info[0]
    event_number = int(event_info[1])

    if event_type == "rest":
        if energy >= 100:
            energy = 100
            print(f"You gained 0 energy.")
        else:
            energy += event_number
            print(f"You gained {event_number} energy.")

        print(f"Current energy: {energy}.")

    elif event_type == "order":
        if energy >= 30:
            print(f"You earned {event_number} coins.")
            energy -= 30
            coins += event_number
        else:
            energy += 50
            print("You had to rest!")
    else:
        if coins >= event_number:
            print(f"You bought {event_type}.")
            coins -= event_number
        else:
            print(f"Closed! Cannot afford {event_type}.")
            closed_condition = True
            break

if not closed_condition:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
