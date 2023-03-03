inp = input().split()
command = input()
while command != '3:1':
    instruction = command.split()
    if instruction[0] == 'merge':
        start = int(instruction[1])
        end = int(instruction[2])
        inp[start:end+1] = [''.join(inp[start:end+1])]
        command = input()

    elif instruction[0] == "divide":
        index = int(instruction[1])
        partitions = int(instruction[2])
        if partitions > len(inp[index]):
            step = 1
        else:
            step = len(inp[index]) // partitions
        divide_part = inp.pop(index)
        start = 0
        for parts in range(partitions):
            if parts == partitions - 1:
                inp.insert(index, divide_part[start::])
                break
            else:
                inp.insert(index, divide_part[start: start + step:])
                start += step
                index += 1
    command = input()
print(inp)
