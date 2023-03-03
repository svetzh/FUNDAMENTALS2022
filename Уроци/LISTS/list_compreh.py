# fruits = ["apples", "bananas", "strawberries"]

# # with for loop way
# new_fruits = []
# for fruit in fruits:
#     fruit = fruit.upper()
#     new_fruits.append(fruit)
# fruits = new_fruits
# print(fruits)

# with list comprehension way
# fruits = [fruit.upper() for fruit in fruits]
# print(fruits)

# my_string = "HelloMyNameIsSvetlio"
# my_string = "".join([i if i.islower() else " " + i.lower() if i in ["N", "I"] else " " + i for i in my_string])[1:]
# print(my_string)
