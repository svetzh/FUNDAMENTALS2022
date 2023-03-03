# inventory = ["sword", "shield", "potion"]
# # 1 get numbers from
# for slot in range(len(inventory)):
#     item = inventory[slot]
#     print(f"{slot}: {item}")

# 2 (try with enumerate the same result)
# for slot, item in enumerate(inventory):
#     print(f"{slot}: {item}")

initial_values = [int(x) for x in input().split()]

raw_input = input()
while raw_input != "end":
    action_args = raw_input
    line = action_args.split()
    action = line[0]

    if action == "swap":
        index1 = int(line[1])
        index2 = int(line[2])
        initial_values[index1], initial_values[index2] = \
            initial_values[index2], initial_values[index1]

    elif action == "multiply":
        index1 = int(line[1])
        index2 = int(line[2])
        multi_product = initial_values[index1] * initial_values[index2]
        initial_values.pop(index1)
        initial_values.insert(index1, multi_product)

    elif action == "decrease":
        initial_values = [x - 1 for x in initial_values]

    raw_input = input()

print(*initial_values, sep=', ')
