command = input()
while command != "Welcome!":
    if command == "Voldemort":
        print("You must not speak of that name!")
        break
    name = len(command)
    if name < 5:
        print(f'{command} goes to Gryffindor.')
    elif name == 5:
        print(f"{command} goes to Slytherin.")
    elif name == 6:
        print(f"{command} goes to Ravenclaw.")
    elif name > 6:
        print(f"{command} goes to Hufflepuff.")
    command = input()

if command == "Welcome!":
    print("Welcome to Hogwarts.")
