def get_chars(first_char, second_char):
    collected_chars = []
    for curr_char in range(ord(first_char) + 1, ord(second_char)):
        collected_chars.append(chr(curr_char))
    return collected_chars


first_char = input()
second_char = input()
result = get_chars(first_char, second_char)
print(' '.join(result))
print(type(result))
