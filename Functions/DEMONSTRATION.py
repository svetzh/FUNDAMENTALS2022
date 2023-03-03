# import os
# os.remove("12_factorial_division.py")  # -- > this way I can remove files directly from the current folder

# numbers = input().split()
# numbers_list = [float(x) for x in numbers]
#
# print(numbers_list)

# numbers = list(map(float, input().split(' ')))
# result = [abs(num) for num in numbers]
# print(result)

#####################################
# 1st variant:
'''

def give_me_five() :
    return 5


def person(first_name = "George
, last_name = "Brownpr:
print(first_name, last_name)

person("Peterint(give_me_five())


# 2st variant:
def give_me_six():
    print(6)


give_me_six()
'''
#####################################

# Default arguments

# def person(first_name="George", last_name="Brown"):
#     print(first_name, last_name)
#
#
# person()  # person("Peter")
#
# # keyword arguments
#
# def area(a, b):
#     return a * b
#
#
# print(area(4, 5))
#
#
# def area_sq(c=2, d=3):
#     print(c * d)
#
#
# area_sq()
#####################################

# def calculation_fund(number_a, number_b, operation):
#     if operation == "multiply":
#         return number_a * number_b
#     elif operation == "divide":
#         return number_a // number_b
#     elif operation == "add":
#         return number_a + number_b
#     elif operation == "subtract":
#         return number_a - number_b
#
#
# type_of_operation = input()
# first_number = int(input())
# second_number = int(input())
# print(calculation_fund(first_number, second_number, type_of_operation))

# #####################################
#
#DOCSTRING:
# def example_func():
#     """This is func just say "Hello\""""
#     return "Hello Svet"
#
#
# print(example_func.__doc__)

#######################################

# x = lambda a: a + 10
# print(x(5))
# # a: --> argument
# # a + 10 --> expression - result
#
# subtr_nums = lambda num1, num2, num3, num4: num1 - num2 - num3 - num4
# print(subtr_nums(100, 20, 10, 5))

#######################################
# result = (list(map(lambda x: round(float(x)), input().split(' '))))
# print(result)
