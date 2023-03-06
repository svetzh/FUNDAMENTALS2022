chars = input().split(", ")
res = {c: ord(c) for c in chars}  # --> dictionary comprehension
print(res)

# # one liner:
# print({c: ord(c) for c in input().split(", ")})
