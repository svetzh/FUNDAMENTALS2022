def selection_course(wish):  # parameter
    if wish.find("sports") != -1:
        course = "volleyball"
    elif wish.find("science") != -1:
        course = "astronomy"
    elif wish.find("comics") != -1:
        course = "sketching"
    else:
        course = "history of ancient Rome"
    return course


number_of_students = int(input("Enter number of students: "))
for student in range(number_of_students):
    wish = input("Enter your wish: ")  # variable
    course = selection_course(wish)  # argument
    print(f"Recommended:{course}")

    if course == "astronomy":
        print("Warning! Classes are held at night!")
