my_list_1 = [32, 14, 45, 33]
my_list_2 = my_list_1
my_list_2.pop()
print(my_list_2)
print(my_list_1)

my_list_1 = [32, 14, 45, 33]
my_list_2 = my_list_1.copy()
my_list_2.pop()
print(my_list_2)
print(my_list_1)
