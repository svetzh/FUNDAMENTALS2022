employee_1_processed = int(input())
employee_2_processed = int(input())
employee_3_processed = int(input())
all_students = int(input())

hours = 0

while all_students > 0:
    hours += 1
    if hours % 4 == 0:
        continue

    all_students -= (employee_1_processed + employee_2_processed + employee_3_processed)

print(f"Time needed: {hours}h.")
