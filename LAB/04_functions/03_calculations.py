# operator = input()
# first_num = int(input())
# second_num = int(input())
#
#
# def solve(a, b, some_operator):
#     result = None
#     if some_operator == "multiply":
#         result = a * b
#     elif some_operator == 'divide':
#         result = a // b
#     elif some_operator == 'add':
#         result = a + b
#     elif some_operator == 'subtract':
#         result = a - b
#     return result
#
#
# print(solve(first_num, second_num, operator))

def simple_operator(operator, num_1, num_2):
    if operator == "multiply":
        return num_1 * num_2
    elif operator == "divide":
        return num_1 // num_2
    elif operator == "add":
        return num_1 + num_2
    elif operator == "subtract":
        return num_1 - num_2


operator = input()
num_1 = int(input())
num_2 = int(input())
print(simple_operator(operator, num_1, num_2))
