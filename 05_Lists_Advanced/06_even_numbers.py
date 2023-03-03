nums_as_string = input().split(', ')
nums = [int(el) for el in nums_as_string]  # output -> [3, 2, 1, 5, 8]

filtered_nums = [idx for idx in range(len(nums)) if nums[idx] % 2 == 0]
print(filtered_nums)
