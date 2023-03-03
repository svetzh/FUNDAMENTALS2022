waiting_persons = int(input())
current_space_available = input().split()
current_space_available = list(map(int, current_space_available))
lift = []
q = 0
result_int = waiting_persons // len(current_space_available)

for i in range(len(current_space_available)):

    if current_space_available[i] > 0 and current_space_available[i] < 3:
        wagon = 4 - int(current_space_available[i])
        wagon += current_space_available[i]
        lift.append(wagon)
    else:
        lift.append(4)

sum_people = waiting_persons - sum(lift)
print(lift)