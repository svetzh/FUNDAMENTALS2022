def factorial(n):
    if n == 0:
        return 1

    return n * factorial(n - 1)


x = int(input())
y = int(input())
x_res = factorial(x)
y_res = factorial(y)
print(f"{x_res / y_res:.2f}")
