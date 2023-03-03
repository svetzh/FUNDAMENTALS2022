key = int(input())
number_of_letters = int(input())

for i in range(number_of_letters):
    letter = input()
    added_key = ord(letter) + key
    print(chr(added_key), end='')
