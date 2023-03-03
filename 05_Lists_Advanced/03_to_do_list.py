notes = [0] * 10
command = input()
while command != "End":
    tokens = command.split('-')
    importance = int(tokens[0]) - 1
    note = tokens[1]

    notes.insert(importance, note)
    command = input()

result = [el for el in notes if el != 0]
print(result)
