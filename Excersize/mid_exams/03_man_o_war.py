# pirate_ship = list(map(int, input().split(">")))
# warship = list(map(int, input().split(">")))
# max_health = int(input())
# is_sunk = False
# min_health_limit = max_health * .2
# def is_valid(index, limit):
#     return 0 <= index < limit
#
#
# command = input().split()
# while command[0] != "Retire" and not is_sunk:
#     action = command[0]
#
#     if action == "Fire":
#         index = int(command[1])
#         damage_p = int(command[2])
#         if is_valid(index, len(warship)):
#             warship[index] -= damage_p
#             if warship[index] <= 0:
#                 print("You won! The enemy ship has sunken.")
#                 is_sunk = True
#                 breakп
#     elif action == "Defend":
#         start_index = int(command[1])
#         end_index = int(command[2])
#         damage = int(command[3])
#         if is_valid(start_index, len(pirate_ship)) \
#                 and is_valid(start_index, len(pirate_ship)):
#             for i in range(start_index, end_index + 1):
#                 pirate_ship[i] -= damage
#                 if pirate_ship[i] <= 0:
#                     print("You lost! The pirate ship has sunken.")
#                     is_sunk = True
#                     break
#     elif action == "Repair":
#         index = int(command[1])
#         health = int(command[2])
#         if is_valid(index, len(pirate_ship)):
#             pirate_ship[index] += health
#             if pirate_ship[index] > max_health:
#                 pirate_ship[index] = max_health
#     else:
#         count = 0
#         for element in pirate_ship:
#             if element < min_health_limit:
#                 count += 1
#         print(f"{count} sections need repair.")
#
#     command = input().split()
#
# sum_pirate_ship = sum(pirate_ship)
# sum_man_o_war = sum(warship)
#
# if not is_sunk:
#     print(f"Pirate ship status: {sum_pirate_ship}")
#     print(f"Warship status: {sum_man_o_war}")

# for el in pirate_ship_section_nums:
#     sum_pirate_ship += el
# for elem in war_ship_section_nums:
#     sum_man_o_war += elem
################################################################################
def is_valid_idx(idx, seq):
    return 0 <= idx < len(seq)


pirate_ship = [int(x) for x in input().split('>')]
war_ship = [int(x) for x in input().split('>')]
max_health = int(input())

is_running = True

while is_running:
    line = input()

    if line == "Retire":
        break

    command_args = line.split()
    command = command_args[0]

    # {} sections need repair.

    if command == "Fire":
        idx = int(command_args[1])
        damage = int(command_args[2])
        if not is_valid_idx(idx, war_ship):
            continue
        war_ship[idx] -= damage
        if war_ship[idx] <= 0:
            is_running = False
            print(f"You won! The enemy ship has sunken.")

    elif command == "Defend":
        start_idx = int(command_args[1])
        end_idx = int(command_args[2])
        damage = int(command_args[3])
        if not is_valid_idx(start_idx, pirate_ship) or not is_valid_idx(end_idx, pirate_ship):
            continue
        for idx in range(start_idx, end_idx + 1):
            pirate_ship[idx] -= damage
            if pirate_ship[idx] <= 0:
                print("You lost! The pirate ship has sunken.")
                is_running = False
                break

    elif command == "Repair":
        idx = int(command_args[1])
        health = int(command_args[2])
        if not is_valid_idx(idx, pirate_ship):
            continue
        pirate_ship[idx] = min(max_health, pirate_ship[idx] + health)  # --> takes the min value between the two results

    elif command == "Status":
        threshold = max_health * .2
        counter = 0
        for section in pirate_ship:
            if section < threshold:
                counter += 1

        print(f"{counter} sections need repair.")

if is_running:
    print(f"Pirate ship status: {sum(pirate_ship)}")
    print(f"Warship status: {sum(war_ship)}")





