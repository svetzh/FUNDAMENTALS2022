n = int(input())
sum_char = 0
for i in range(n):
    char = input()
    char_num = ord(char)
    sum_char += char_num
print(f"The sum equals: {sum_char}")
