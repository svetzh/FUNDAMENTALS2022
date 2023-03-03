def merge_element(elements, start, end):
    merge_result = ""
    for i in range(start, end + 1):
        merge_result += elements[i]
    return merge_result

words = input().split()

while True:
    line = input()
    if line == "3:1":
        break

    command, first_arg, second_arg = line.split()

    if command == "merge":
        start_idx = int(first_arg)
        end_idx = int(second_arg)

        start_idx = max(0, start_idx)
        end_idx = min(len(words) - 1, end_idx)

        if start_idx >= end_idx:
            continue

        merged_element = merge_element(words, start_idx, end_idx)
        remove_count_ops = end_idx - start_idx + 1
        for _ in range(remove_count_ops):
            words.pop(start_idx)
        words.insert(start_idx, merged_element)

    elif command == "divide":
        index = int(first_arg)
        partitions = int(second_arg)

        element = words[index]
        elements_parts = []
        partition_size = len(element) // partitions

        current_partition = ""
        for idx in range((partitions - 1) * partition_size):
            current_partition += element[idx]
            if len(current_partition) == partition_size:
                elements_parts.append(current_partition)
                current_partition = ""
        current_partition = ""
        for idx in range((partitions - 1) * partition_size, len(element)):
            current_partition += element[idx]
        elements_parts.append(current_partition)
        words.pop(index)

        for i in range(len(elements_parts)):
            words.insert(index + i, elements_parts[i])

        print()

print(" ".join(words))
