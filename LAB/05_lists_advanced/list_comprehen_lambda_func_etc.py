# integers = [1, 2, 3]
# strings = [str(integer) for integer in integers]
# a_string = "".join(*strings)
# an_integer = int(a_string)
#
# print(a_string)

# x = list(set((311, 341, 876)))
# print(x)

# earth_metals = ["Berillium", "Magnesium", "Calcium", "Strontium", "Barium", "Radium"]
# earth_metals.sort()

# format := (name, radius, density, distance from Sun "AU")
# planets = [("Mercury", 2440, 5.43, 0.394),
#            ("Venus", 6052, 5.24, 0.723),
#            ("Earth", 6378, 5.52, 1.000),
#            ("Mars", 3396, 3.93, 1.530),
#            ("Jupiter", 71492, 1.33, 5.210),
#            ("Saturn", 60268, 0.69, 9.551),
#            ("Uranus", 25559, 5.52, 19.213),
#            ("Neptune", 24764, 1.64, 30.070),
#            ]
# size_p = lambda planet: planet[1]
# planets.sort(key=size_p, reverse=True)
# print(planets, '\n')
#
# density = lambda planet: planet[0]
# planets.sort(key=density)
# print(planets)
#
# # The most distant from SUN AU
# distance = lambda planet: planet[3]
# planets.sort(key=distance)
# print(planets[-1])
#
# nums = [85, 15, 35, 35, 78, 41, 9]
# strs_names = input().split(", ")
# print(nums)
# print(nums.index(35))
# nums.reverse()
# print(nums)
# nums.reverse()
# print(nums)
# print(nums.index(35))
# print("--------------------")
# rev_nums = list(reversed(nums))
# print(rev_nums)
# print("--------------------")
# for index in range(len(nums) - 1, -1, -1):
#     if nums[index] == 35:
#         print(index)
#         break

# new_nums_reversed = list(reversed(nums))
# print(new_nums_reversed)
# print(nums[::-1])
# l_ordered = sorted(nums, key=lambda x: x, reverse=True)
#
# print(sorted(strs_names, key=lambda x: -len(x)))  # --> sorted by descending order
# print(sorted(strs_names, key=lambda x: (-len(x), x)))  # --> sorted by descending and by ASCII first

# numbers = input().split(", ")
# even_numbers = [int(num) for num in numbers if int(num) % 2 == 0]
# '''
# --> 1. iterate through numbers and
# --> 2. cast num to int, and if this integer is even
# --> 3. put it like an integer in the list (if is odd - False we don't put it)
# '''
# print(even_numbers)

# numbers = input().split(", ")
# indexed_numbers = [int(index) for index in range(len(numbers)) if int(numbers[index]) % 2 == 0]
# print(indexed_numbers)
#
# nums = [85, 78, 41, 35, 35, 15, 8]
# print([i for i, k in enumerate(nums) if k % 2 == 0])

# b = [1, 2, 3]
# print(*b, sep='->')
# nums = [85, 78, 41, 35, 35, 15, 8]
# print([i for i, k in enumerate(nums) if k % 2 == 0])
# nums = input().split(", ")
# print([int(i) for i, k in enumerate(nums) if int(k) % 2 == 0])

# swap_nums = [43, 18, 29]
# swap_nums[0], swap_nums[1], swap_nums[2] = swap_nums[2], swap_nums[0], swap_nums[1]
# print(swap_nums)
#
# ex_nums = [13, 14, 15]
# ex_nums_2 = [16, 17, 18]
# ex_nums.extend(ex_nums_2)
# print(ex_nums)
# result = ex_nums + ex_nums_2
# print(result)
# result_set = list(set(ex_nums))
# result_set.extend(ex_nums_2)
# print(result_set)


bla_list = ["Cat", "Dog", "Bird", "Fish", "Pig"]
bla_list[1], bla_list[3] = bla_list[3], bla_list[1]
print(bla_list)











