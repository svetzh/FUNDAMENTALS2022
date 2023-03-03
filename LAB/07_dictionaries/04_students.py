# searched_course = None
# courses = {}
#
# while True:
#     command_input = input()
#
#     if ":" not in command_input:
#         searched_course = command_input
#         break
#
#     command_args = command_input.split(":")
#     name = command_args[0]
#     id = command_args[1]
#     course = command_args[2]
#
#     if course not in courses:
#         courses[course] = {}
#
#     courses[course][id] = name
# searched_course = searched_course.replace("_", " ")
#
# for k, v in courses[searched_course].items():
#     print(f"{v} - {k}")

data = input()

courses = {}

while ":" in data:
    student_name, student_id, course_name = data.split(":")
    if course_name not in courses:
        courses[course_name] = {student_id: student_name}
    else:
        courses[course_name][student_id] = student_name
    data = input()

# course_name = " ".join(data.split("_"))
course_name = data.replace("_", " ")


students = courses[course_name]
for student_id, name in students.items():
    print(f"{name} - {student_id}")






