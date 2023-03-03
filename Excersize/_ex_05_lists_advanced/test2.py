# greeting = lambda: print("Hello World!")
# greeting()
#
# def greeting():
#     print("Hello World")
# greeting()
#
# greeting_with_name = lambda name: print("Hey there, " + name)
# greeting_with_name("Sandra")
#
# str1 = 'I say Hello World'
# up_str = lambda x: x.upper()[::2]
# print(up_str(str1))
# n = 5
# for i in range(1, n + 1):
#     for j in range(i - 1):
#         print(" ", end=" ")
#     for j in range(2*(n-i) + 1):
#         print("*", end="")
# #     print()
# a = 5
# for i in range(1, a + 1):
#     print("" * (i - 1), end="")
#     print("*" * (2 * (a-i) + 1))

# def some_fun():
#     return 2, 4, 6
#
# print(*some_fun())
#
# print((lambda a, b, c: a * b * c)(1, 2, 3))
# for i, v in enumerate("smotanqk"):
#     print(i, v, end=" ")

# string = "Solomon so of, alibi in to cash"
# bad_str = string[::3]
# print(bad_str)

###########################################

# command = input()
# total_price = 0
# counter = 1
# while True:
#     if counter == 1 and (command == "regular" or command == "special"):
#         print("Invalid order!")
#         exit()
#     else:
#         while command != "regular" and command != "special":
#             price = float(command)
#             if price < 0:
#                 print("Invalid price!")
#             else:
#                 total_price += price
#             command = input()
#
#         print("Congratulations you've just bought a new computer!")
#         print(f"Price without taxes: {total_price:.2f}$")
#         tax = total_price * .2
#         print(f"Taxes: {tax:.2f}$")
#         print("-----------")
#
#         total_price += tax
#         if command != "special":
#             print(f"Total price: {total_price:.2f}$")
#         else:
#             print(f"Total price: {(total_price * .9):.2f}$")
#         if total_price == 0:
#             print("Invalid order!")
#     counter += 1
#     if counter > 1:
#         break

rooms = int(input())

free_chairs = 0
game_on = True
for room in range(1, rooms + 1):
    chairs, guests_as_str = input().split()
    guests = int(guests_as_str)

    if guests > len(chairs):
        needed_chairs = guests - len(chairs)
        print(f'{needed_chairs} more chairs needed in room {room}')
        game_on = False
    else:
        free_chairs_by_row = len(chairs) - guests
        free_chairs += free_chairs_by_row
if game_on:
    print(f"Game On, {free_chairs} free chairs left")
















