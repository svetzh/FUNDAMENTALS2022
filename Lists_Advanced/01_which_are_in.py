first_word_sequence = input().split(", ")
second_word_sequence = input().split(", ")
result = []

for el in first_word_sequence:
    for i in second_word_sequence:
        if el in i:
            result.append(el)
            break

print(result)

# nested list comprehension
