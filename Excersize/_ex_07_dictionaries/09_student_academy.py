rows = int(input())
students_grades_journal = {}

count = 0
for _ in range(rows):
    student = input()
    student_grade = float(input())

    if student not in students_grades_journal:
        students_grades_journal[student] = []
    students_grades_journal[student].append(student_grade)

for student, grades in students_grades_journal.items():
    average_grade = sum(grades) / len(grades)
    if average_grade >= 4.5:
        print(f"{student} -> {average_grade:.2f}")
    else:
        continue

