number_of_users = int(input("Enter number of students: "))
for user in range(number_of_users):
    login = input("Enter students name: ")
    age = int(input("Input age: "))
    if age < 14:
        print("Error: less than 14 years old.")
    else:
        print(f"Account created: {login}")
