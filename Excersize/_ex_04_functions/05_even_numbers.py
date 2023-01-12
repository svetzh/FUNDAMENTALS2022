# 1-st VARIANT:
# numbers_as_string = input().split(" ")
# numbers_as_digits = []
# for number in numbers_as_string:
#     numbers_as_digits.append(int(number))

# 2-nd VARIANT:
# numbers_as_digits = [int(s) for s in input().split()]
# is_even = lambda x: x % 2 == 0
# result = list(filter(is_even, numbers_as_digits))
# print(result)



numbers = [int(x) for x in input().split()]
even_nums_only = lambda number: number % 2 == 0

result = list(filter(even_nums_only, numbers))  # --> filter "even_nums_only" from numbers
print(result)