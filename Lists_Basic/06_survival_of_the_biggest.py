number_str_list = input().split()
n = int(input())
number_digit = []
for element in range(len(number_str_list)):
    number_digit.append(int(number_str_list[element]))

for i in range(n):
    min_element = min(number_digit)
    number_digit.remove(min_element)

for i in range(len(number_digit)):
    number_digit[i] = str(number_digit[i])

print(', '.join(number_digit))
