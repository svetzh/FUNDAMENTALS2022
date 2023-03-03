num_list_int = [int(num) for num in input().split(", ")]

positive_lst = [i for i in num_list_int if i >= 0]
negative_lst = [i for i in num_list_int if i < 0]
odd_lst = [i for i in num_list_int if i % 2 != 0]
even_lst = [i for i in num_list_int if i % 2 == 0]


pos_str = list(map(str, positive_lst))
pos = ", ".join(pos_str)

neg_str = list(map(str, negative_lst))
neg = ", ".join(neg_str)

od_str = list(map(str, odd_lst))
od = ", ".join(od_str)

ev_str = list(map(str, even_lst))
ev = ", ".join(ev_str)

print(f"Positive: {pos}")
print(f"Negative: {neg}")
print(f"Even: {ev}")
print(f"Odd: {od}")

