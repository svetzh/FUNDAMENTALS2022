# first way
from math import sqrt

num = int(input())

prime_flag = 0

if num > 1:
    for i in range(2, int(sqrt(num)) + 1):
        if (num % i) == 0:
            prime_flag = 1
            break
    if prime_flag == 0:
        print("True")
    else:
        print("False")
else:
    print("False")

################################
# second way
num = int(input())

prime_flag = True

if num > 1:
    for i in range(2, int(sqrt(num)) + 1):
        if (num % i) == 0:
            prime_flag = False
            break
    if not prime_flag:
        print(prime_flag)
    else:
        print(prime_flag)
else:
    print(prime_flag)