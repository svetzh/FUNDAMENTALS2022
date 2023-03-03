n = int(input())

positive_nums = []
negative_nums = []

for i in range(n):
    curr_num = int(input())
    if curr_num >= 0:
        positive_nums.append(curr_num)
    else:
        negative_nums.append(curr_num)
print(positive_nums)
print(negative_nums)
print(f"Count of positives: {len(positive_nums)}." 
      f" Sum of negatives: {sum(negative_nums)}")