number_lines = int(input())
people_registered = dict()
for _ in range(number_lines):
    raw_data = input().split()
    reg_unreg_command = raw_data[0]
    username = raw_data[1]
    if reg_unreg_command == "register":
        licence_plate = raw_data[2]
        if username not in people_registered:
            people_registered[username] = licence_plate
            print(f"{username} registered {licence_plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {licence_plate}")
    elif reg_unreg_command == "unregister":
        if username not in people_registered:
            print(f"ERROR: user {username} not found")
        else:
            print(f"{username} unregistered successfully")
            del people_registered[username]

for k, v in people_registered.items():
    print(f"{k} => {v}")