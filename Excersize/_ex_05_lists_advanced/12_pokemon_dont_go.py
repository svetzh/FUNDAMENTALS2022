initial_sequence = [int(x) for x in input().split()]
points = 0

while initial_sequence:
    index = int(input())
    if 0 <= index < len(initial_sequence):
        num = initial_sequence.pop(index)
    elif index < 0:
        num_to_add = initial_sequence[-1]
        num = initial_sequence[0]
        initial_sequence[0] = initial_sequence[-1]
    else:
        num_to_add = initial_sequence[0]
        num = initial_sequence[-1]
        initial_sequence[-1] = initial_sequence[0]
    points += num

    for current_index, current_num in enumerate(initial_sequence):
        if current_num <= num:
            initial_sequence[current_index] += num
        else:
            initial_sequence[current_index] -= num

print(points)




