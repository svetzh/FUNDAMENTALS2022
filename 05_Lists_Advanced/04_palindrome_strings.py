all_palindromes = [word for word in input().split() if word == word[::-1]]
searched_palindrome = input()

print(all_palindromes)
print(f"Found palindrome {all_palindromes.count(searched_palindrome)} times")

# #  1. Slicing
# s = "Python"  # initial string
# string_length = len(s)  # calculate length of the list
# sliced_string = s[string_length::-1]  # slicing
# print(sliced_string)  # print the reversed string
# #  2. Loop
# s = "Python"  # initial string
# reversedString = []
# index = len(s)  # calculate length of string and save in index
# while index > 0:
#     reversedString += s[index - 1]  # save the value of str[index-1] in reverseString
#     index = index - 1  # decrement index
# print(reversedString)
#
# #  3. Use Join method
# s = 'Python'  # initial string
# reverse_pal = ''.join(reversed(s))  #.join() # method merges all of the characters resulting from the reversed iteration into a new string
# print(reverse_pal)

