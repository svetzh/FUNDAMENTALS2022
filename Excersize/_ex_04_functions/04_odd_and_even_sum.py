def sum_even_and_odd(num: str):
    odd_sum = 0
    even_sum = 0

    for ch in num:
        digit = int(ch)
        if digit % 2 == 1:
            odd_sum += digit
        elif digit % 2 == 0:
            even_sum += digit

    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"


single_number = input()
result = sum_even_and_odd(single_number)
print(result)
