message = int(input("Enter the current time in hours: "))

while message >= 10 and message < 24:
    print("We're open.")
    message = int(input("Enter the current time in hours: "))
print("We're closed")