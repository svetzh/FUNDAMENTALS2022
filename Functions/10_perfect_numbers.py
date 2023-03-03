def is_perfect(num):
    prop_div = []
    for divisor in range(1, num):
        if num % divisor == 0:
            prop_div.append(divisor)

    if sum(prop_div) == num:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")
    return num


number = int(input())
is_perfect(number)

#
# def perfect_number(num):
#     prop_div = []
#     for n in range(1, + num):
#         if num % n == 0:
#             prop_div.append(n)
#     if sum(prop_div) == num:
#         print("We have a perfect number!")
#     else:
#         print("It's not so perfect.")
#     return num
#
#
# number = int(input())
# perfect_number(number)