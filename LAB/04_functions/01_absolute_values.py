# 1: --> base way

# numbers = input().split()
# abs_numbers = []
# for element in numbers:
#     abs_numbers.append(abs(float(element)))
# print(abs_numbers)

# 2: --> list comprehension

# numbers = list(map(float, input().split()))
# result = [abs(num) for num in numbers]
# print(numbers)

# 3: --> functions
def abs_numbers(nums):
    result = [abs(num) for num in nums]
    return result


numbers = list(map(float, input().split()))
print(abs_numbers(numbers))
