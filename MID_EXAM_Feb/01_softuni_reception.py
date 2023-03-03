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

# first_emploee = int(input())
# second_emploee = int(input())
# third_emploee = int(input())
#
# people_count = int(input())
# people_per_hour = first_emploee + second_emploee + third_emploee
#
# hours = 0
# while people_count > 0:
#     hours += 1
#     people_count -= people_per_hour
#
#     if hours % 4 == 0:
#         hours += 1
# print(f"Time needed: {hours}h.")