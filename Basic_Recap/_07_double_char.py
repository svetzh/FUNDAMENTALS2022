command = input()
while not command == "End":
    if not command == "SoftUni":
        for char in command:
            print(char * 2, end='')
        print()
    command = input()