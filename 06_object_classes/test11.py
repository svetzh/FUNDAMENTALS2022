# class MyClassPerson:
#     def __init__(self, first_name, last_name="Svetoslavov", age=35):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#
#
# ivan = MyClassPerson("Ivan", "Ivanov", 40)
#
# print(ivan.first_name)
# print(ivan.last_name)
# print(ivan.age)
#
# georgi = MyClassPerson(first_name="Ivo", age=55)
# print(georgi.first_name)
# print(georgi.last_name)
# print(georgi.age)

# class Person:
#     def __init__(self, first_name, last_name, age=35):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#
#     def say_hello(self, school1):
#         return f"Hello {self.first_name} {self.last_name} from {school1}"
#
#
# ivan = Person("Ivan", "Ivanchev", 33)
# maria = Person("Maria", "Stoyanova")
# print(ivan.say_hello(school1="Levski"))


# PATTERNS #################################
n = 5
# for i in range(n):
#     for j in range(n):
#         print("*", end=" ")
#     print()
# """
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# """

##########################################

# for i in range(n):
#     for j in range(i):
#         print("*", end=" ")
#     print()
# """
# *
# * *
# * * *
# * * * *
# * * * * *
# """
##########################################

# for i in range(n - 1, -1, -1):
#     for j in range(i):
#         print("*", end=" ")
#     print()

# """
# * * * *
# * * *
# * *
# *
# """
##########################################

# for i in range(n):
#     for j in range(i, n):
#         print("*", end=" ")
#     print()

##########################################

# for i in range(n):
#     for j in range(i):
#         print("*", end=" ")
#     print()
#
# for i in range(n):
#     for j in range(i, n):
#         print("*", end=" ")
#     print()

'''
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
* 
'''
##########################################
for i in range(n):
    for j in range(i, n):
        print("", end="")

    for j in range(i):
        print("*", end="")

    for j in range(i+1):
        print("*", end="")

    print()