def sum_numbers(first_number, second_number):
    sum_result = first_number + second_number
    return sum_result


def subtract(sum_result, third_number):
    substr = sum_result - third_number
    return substr


def add_and_subtract(first_number, second_number, third_number):
    sum_of_first_and_sec_ints = sum_numbers(first_number, second_number)
    subtracting_result = subtract(sum_of_first_and_sec_ints, third_number)
    return subtracting_result


first_number = int(input())
second_number = int(input())
third_number = int(input())

print(add_and_subtract(first_number, second_number, third_number))
