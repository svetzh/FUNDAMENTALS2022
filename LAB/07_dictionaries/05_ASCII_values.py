chars = input().split(", ")
res = {c: ord(c) for c in chars}  # --> dictionary comprehension
print(res)
print({c: ord(c) for c in input().split(", ")})
