# lst_str = input().split(', ')
# without_zero = [x for x in lst_str if x != 0]

# test_list = ['3', '5', '7', '9', '11']
#
# test_list.append(test_list.pop(test_list.index(5)))
# print("The modified element moved list is : " + str(test_list))

# test_list = input().split(', ')
# int_test_lst = []
# len_lst = len(test_list)
# for el in test_list:
#     count = 0
#     if el != int_test_lst:
#         int_test_lst.append(el)
# print(int_test_lst)

# rem_zeroes = [i for i in test_list if i == "0"]
# # print(count_zeroes)
# # print(test_list)
# test_list.insert(count_zeroes, '0')
# print(test_list)
# #
# lst = [eval(y) for y in test_list]
#
# print(lst)

# test_list = input().split(', ')
# elem = "0"
# int_list = list(map(int, test_list))


# test_list = [1, 3, 4, 6, 5, 1]
# ele = 1
# a = list(map(str, test_list))
# print(a)
# b = " ".join(a)
# # print(b)
# b = b.replace(str(ele), "")
# # print(b)
# b = b.split()
# # print(b)
# x = list(map(int, b))
# print(x)


lst_s = input().split(", ")
lst_n = list(map(int, lst_s))
# lst_n = [int(el) for el in lst_s]
n = len(lst_n)
j = 0
for i in range(n):
    if lst_n[i] != 0:
        print("j", j)
        print('i', i)
        lst_n[j], lst_n[i] = lst_n[i], lst_n[j]
        j += 1

print(lst_n)

# list1 = [x for x in lst_s if x != "0"]
# list2 = [y for y in lst_s if y == "0"]
# list_conc = list1 + list2
# print(list(map(int, list_conc)))
