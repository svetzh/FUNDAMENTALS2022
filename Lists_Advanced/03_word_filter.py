words = input().split()
list_word = [x for x in words if len(x) % 2 == 0]

# print(*list_word, sep='\n')
print('\n'.join(list_word))