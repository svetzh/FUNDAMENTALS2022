def check_idx_is_valid(idx, len_list):
    if idx in range(len_list):
        return True
    return False


targets = [int(x) for x in input().split()]
command_data = input()
while command_data != "End":
    command, index, value = command_data.split()
    index = int(index)
    value = int(value)
    if command == "Shoot":
        if check_idx_is_valid(index, len(targets)):
            targets[index] -= value
            if targets[index] <= 0:
                targets.pop(index)
    elif command == "Add":
        if check_idx_is_valid(index, len(targets)):
            targets.insert(index, value)
        else:
            print("Invalid placement!")
    elif command == "Strike":
        left_most_index = index - value
        right_most_index = index + value
        if check_idx_is_valid(index, len(targets)) \
                and check_idx_is_valid(left_most_index, len(targets)) \
                and check_idx_is_valid(right_most_index, len(targets)):
            left_un_striked_part = targets[:left_most_index]
            right_un_striked_part = targets[right_most_index + 1:]
            targets = left_un_striked_part + right_un_striked_part
        else:
            print("Strike missed!")
    command_data = input()

print("|".join(str(i) for i in targets))
