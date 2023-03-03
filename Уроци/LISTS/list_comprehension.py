# # Task 1: Create an empty list and add all letters from the word "human" to it. Print it.
# h_letters = []
# for i in "human":
#     h_letters.append(i)
# print(h_letters)

# # Task 2: Now do it with list comprehension
# h_letters = [x for x in "human"]
# print(h_letters)


# Task 3: Now do it with lambda
# a = (list(map(lambda x: x, "human")))
# print(" ".join(a))
# #Task: Use list comprehension to find and print only the even numbers up to 20
# even_nums = [a for a in range(1, 20) if a % 2 == 0]
# print(even_nums)

# #Task: Print all numbers up to 100 that are divisable by 2 and by 5 (nested if)
# nest = [s for s in range(1, 100) if s % 2 == 0 if s % 5 == 0]
# print(nest)

# #Task: Use a list comprehension to create a list of squares of the numbers between 1 and 10.
# squared_nums = [x * x for x in range(1, 11)]
# print(squared_nums)

# # Task: Each number of the first list must be paired with a number from the second list
# nums1 = [1, 2, 3]
# nums2 = [4, 5, 6]
# new_list = [(x, y) for x in nums1 for y in nums2]
# # print(new_list)
# for el in nums1:
#     for le in nums2:
#         print((el, le), end=" ")

# pirate_ship_section_nums = list(map(int, input().split(">")))
# war_ship_sections_nums = list(map(int, input().split(">")))
# start_idx = 0
# for i in pirate_ship_section_nums:
#     for j_idx, j in enumerate(war_ship_sections_nums[start_idx:], start=start_idx):
#         if j == pirate_ship_section_nums:
#             print('Bingo!')
#             start_idx = j_idx
#             break

#################################################################################################################
pirate_ship_section_nums = list(map(int, input().split(">")))
war_ship_section_nums = list(map(int, input().split(">")))

max_health_section = int(input())
min_health_limit = max_health_section * .2
count = 0
is_sunk = False
stalemate = True

while True:
    if is_sunk:
        exit()

    command = input()
    action_args = command.split()
    action = action_args[0]

    if command == "Retire":
        break

    if action == "Fire":
        index = int(action_args[1])
        damage_p = int(action_args[2])
        if 0 <= index < len(war_ship_section_nums) and damage_p >= 0:
            war_ship_section_nums[index] -= damage_p
            for el in war_ship_section_nums:
                if el <= 0:
                    print("You won! The enemy ship has sunken.")
                    is_sunk = True
                    break
                continue

    elif action == "Defend":
        start_index = int(action_args[1])
        end_index = int(action_args[2])
        damage_w = int(action_args[3])
        if (0 <= start_index < len(pirate_ship_section_nums)) \
                and (0 <= end_index < len(pirate_ship_section_nums)) \
                and damage_w > 0:
            for i in range(start_index, end_index + 1):
                pirate_ship_section_nums[i] -= damage_w
                if pirate_ship_section_nums[i] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    is_sunk = True
                    break

    elif action == "Repair":
        idx = int(action_args[1])
        health = int(action_args[2])
        if 0 <= idx < len(pirate_ship_section_nums) \
                and health <= max_health_section:
            for eli in pirate_ship_section_nums:
                if eli < int(min_health_limit):
                    count += 1
            pirate_ship_section_nums[idx] += health

    elif action == "Status":
        for element in pirate_ship_section_nums:
            if element < min_health_limit:
                count += 1
print(f"{count} sections need repair.")
sum_pirate_ship = sum(pirate_ship_section_nums)
sum_man_o_war = sum(war_ship_section_nums)

if not is_sunk:
    print(f"Pirate ship status: {sum_pirate_ship}")
    print(f"Warship status: {sum_man_o_war}")




