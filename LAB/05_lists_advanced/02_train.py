# n_wagons = int(input())
# wagons = [0] * n_wagons
#
# command = input()
# while command != "End":
#     row_data = command.split()
#     if row_data[0] == "add":
#         wagons[-1] += int(row_data[1])
#     elif row_data[0] == "insert":
#         wagons[int(row_data[1])] += int(row_data[2])
#     elif row_data[0] == "leave":
#         wagons[int(row_data[1])] -= int(row_data[2])
#
#     command = input()
# print(wagons)


n_wagons = int(input())
train = [0] * n_wagons

command = input()
while command != "End":
    action = command.split()
    action = split_data = action[0]

    if action == "add":
    # if command.startswith("add"): --> good method
        n_people = command.split()[1]
        train[-1] += int(command.split()[1])
    elif action == "insert":
        index = int(int(command.split()[1]))
        n_people = int(int(command.split()[2]))
        train[index] += n_people
    elif action == "leave":
        index = int(int(command.split()[1]))
        n_people = int(int(command.split()[2]))
        train[index] -= n_people
    command = input()

print(train)