"""
numbers = input().split()
nums_inverse = []
for number in numbers:
    number_inverted = int(number) * (-1)
    nums_inverse.append(number_inverted)
print(nums_inverse, end=" ")
"""

list_of_numbers = input().split()
opposite_numbers = []
for element in list_of_numbers:
    opposite_numbers.append(-int(element))
print(opposite_numbers)