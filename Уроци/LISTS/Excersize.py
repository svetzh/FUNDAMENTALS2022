# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# e = [x if x > 4 else 'less than 4' for x in lst]
# d = []
# print(e)
# for el in lst:
#     if el > 4:
#         d.append(el)
#     else:
#         d.append('less than 4')
# print(d)
# lst_rev = [6, 4, 2]
# g = [(x, y) for x in lst for y in lst_rev]
# print(g)

# f = []
# for x in lst:
#     for y in lst_rev:
#         f.append((y, x))
# print(f)

# def g(x=5, y=0):
#     return x + y
#
#
# print(g(y=5))

# arr = [1, 2, 3]
# arr[0:0] = [0]
# print(arr)

names = ["Kelly", "Nelly", "Jimmy", "Lenny"]
for num, name in enumerate(names, start=1):
    print(num, name)
