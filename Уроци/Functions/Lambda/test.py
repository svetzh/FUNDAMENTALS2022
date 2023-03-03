# # Write a lambda function to add up 3 numbers
# add_up_number = lambda x, y, z: x + y + z
# print(add_up_number(3, 8, 1))
#
# # Write a lambda function to multiply 3 numbers
# mult_num = (lambda a, b, c: a * b * c)(1, 2, 3)
# print(mult_num)
#
# # cube a number
# cube_num = lambda e: e ** 3
# print(cube_num(9))

# def numbers(a, b):
# #     if a > b:
# #         return a
# #     else:
# #         return b
# # print(numbers(1, 2))
# # print(numbers(14, 3))
# #
# # max_num = lambda m, n: n if (n > m) else m
# # min_num = lambda m, n: n if (m > n) else m
# # print(max_num(1, 2))
# # print(max_num(14, 3))
# # print(min_num(1, 2))
# # print(min_num(14, 3))

list1 = input().split()
result = ""
for num in list1:
    is_palindrome = num[-0] == num[-1]
    result += str(is_palindrome) + "\n"

print(result)
