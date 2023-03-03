integers = [float(x) for x in input().split()]
result_ints = sum(integers)
length_ints = len(integers)
avg_nums = (result_ints / length_ints)

greater_nums = []
for el in integers:
    if el > avg_nums:
        greater_nums.append(int(el))
greater_nums.sort(reverse=True)

if len(greater_nums[:5]) > 0:
    list_formated = list(map(str, greater_nums[:5]))
    print(" ".join(list_formated))
else:
    print("No")

