import random
number = int(input())
password = ""
for i in range(number):
    password += str(random.randint(0, 9))

print(password)
