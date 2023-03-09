raw_input = input()
courses = {}
while raw_input != "end":
    command = raw_input.split(" : ")
    course_name = command[0]
    user_name = command[1]

    if course_name not in courses:
        courses[course_name] = []
    courses[course_name].append(user_name)

    raw_input = input()

for course_name, user_name in courses.items():
    print(f"{course_name}: {len(user_name)}")

    for student in range(0, len(user_name)):
        print(f"-- {user_name[student]}")
    # # same result as the upper nested for loop
    # for student in user_name:
    #     print(f"-- {student}")

