# n = int(input())
#
# even_nums = []
# odd_nums = []
# positive_nums = []
# negative_nums = []
#
# for _ in range(n):
#     current_num = int(input())
#
#     if current_num % 2 == 0:
#         even_nums.append(current_num)
#     if current_num >= 0:
#         positive_nums.append(current_num)
#     if current_num % 2 == 1:
#         odd_nums.append(current_num)
#     if current_num < 0:
#         negative_nums.append(current_num)
#
# command = input()
#
# if command == "even":
#     print(even_nums)
# elif command == "odd":
#     print(odd_nums)
# elif command == "positive":
#     print(positive_nums)
# else:
#     print(negative_nums)

# fruits = ["apples", "bananas", "strawberries"]
#
# for fruit in fruits:
#     fruit = fruit.upper()
#     new_fruits.append(fruit)
# fruits = new_fruits
# print(fruits)

# ms = "".join([i if i.islower() else " " + i for i in fruits])
# string using list comprehension:
some_string = "HeySvetlioHow Are you?"
new_st = some_string.split()
stripped_str = new_st[0]
stripped_str = "".join([i if i.islower() else " " + i for i in stripped_str])[1:]  # --> using slice at the end
print(stripped_str)




















