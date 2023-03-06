# number_of_snowballs = int(input())
# max_snowball_weight = 0
# max_snowball_time = 0
# max_snowball_quality = 0
# max_snowball_value = 0
#
# for snowball in range(number_of_snowballs):
#     curr_snowball_weight = int(input())
#     curr_snowball_time = int(input())
#     curr_snowball_quality = int(input())
#     curr_snowball_value = (curr_snowball_weight // curr_snowball_time) ** curr_snowball_quality
#
#     if curr_snowball_value > max_snowball_value:
#         max_snowball_weight = curr_snowball_weight
#         max_snowball_time = curr_snowball_time
#         max_snowball_quality = curr_snowball_quality
#         max_snowball_value = curr_snowball_value
#
# print(f"{max_snowball_weight} : {max_snowball_time} = {max_snowball_value} ({max_snowball_quality})")

n = int(input())

best_snowball = float('-inf')
output = ''
for idx in range(n):
    weight = int(input())
    time = int(input())
    quality = int(input())

    result = (weight // time) ** quality

    if result > best_snowball:
        best_snowball = result
        output = f"{weight} : {time} = {result} ({quality})"

print(output)