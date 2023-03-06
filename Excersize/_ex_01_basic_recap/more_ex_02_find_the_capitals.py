text = input()
indexes_list = []
for i in range(len(text)):
    if text[i].isupper():
        indexes_list.append(i)
print(indexes_list)