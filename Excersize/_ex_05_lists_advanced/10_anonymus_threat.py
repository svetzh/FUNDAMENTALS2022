strings_input = input().split()
result = []
instructions = input()
while instructions != "3:1":
    instructions = instructions.split()
    command = instructions[0]
    if command == "merge":
        start = int(instructions[1])
        end = int(instructions[2])
        if start < 0:
            start = 0
        if end > len(strings_input) - 1:
            end = len(strings_input) - 1
        for index, string in enumerate(strings_input):
            if index in range(start + 1, end + 1):
                strings_input[start] += strings_input[index]
        for index in range(end, start, -1):
            strings_input.pop(index)

    elif command == "divide":
        index = int(instructions[1])
        partitions = int(instructions[2])
        if partitions > len(strings_input[index]):
            step = 1
        else:
            step = len(strings_input[index]) // partitions
        divide_part = strings_input.pop(index)
        start = 0
        for parts in range(partitions):
            if parts == partitions - 1:
                strings_input.insert(index, divide_part[start::])
                break
            else:
                strings_input.insert(index, divide_part[start: start + step:])
                start += step
                index += 1
    instructions = input()

print(" ".join(strings_input))

########################################################################################
# def merge_element(elements, start, end):
#     merge_result = ""
#     for i in range(start, end + 1):
#         merge_result += elements[i]
#     return merge_result
#
# words = input().split()
#
# while True:
#     line = input()
#     if line == "3:1":
#         break
#
#     command, first_arg, second_arg = line.split()
#
#     if command == "merge":
#         start_idx = int(first_arg)
#         end_idx = int(second_arg)
#
#         start_idx = max(0, start_idx)
#         end_idx = min(len(words) - 1, end_idx)
#
#         if start_idx >= end_idx:
#             continue
#
#         merged_element = merge_element(words, start_idx, end_idx)
#         remove_count_ops = end_idx - start_idx + 1
#         for _ in range(remove_count_ops):
#             words.pop(start_idx)
#         words.insert(start_idx, merged_element)
#
#     elif command == "divide":
#         index = int(first_arg)
#         partitions = int(second_arg)
#
#         element = words[index]
#         elements_parts = []
#         partition_size = len(element) // partitions
#
#         current_partition = ""
#         for idx in range((partitions - 1) * partition_size):
#             current_partition += element[idx]
#             if len(current_partition) == partition_size:
#                 elements_parts.append(current_partition)
#                 current_partition = ""
#         current_partition = ""
#         for idx in range((partitions - 1) * partition_size, len(element)):
#             current_partition += element[idx]
#         elements_parts.append(current_partition)
#         words.pop(index)
#
#         for i in range(len(elements_parts)):
#             words.insert(index + i, elements_parts[i])
#
#         print()
#
# print(" ".join(words))
