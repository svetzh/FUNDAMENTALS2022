# def not_even_num(x):
#     return x % 2 != 0

# neighborhood = [int(x) for x in input().split("@")]
#
# raw_command = input()
# position = 0
#
# while raw_command != "Love!":
#     length_jump = raw_command.split()[1]
#     length_jump = int(length_jump)
#
#     position += length_jump
#
#     if position >= len(neighborhood):
#         position = 0
#
#     if neighborhood[position] == 0:
#         print(f"Place {position} already had Valentine's day.")
#     else:
#         neighborhood[position] -= 2
#         if neighborhood[position] == 0:
#             print(f"Place {position} has Valentine's day.")
#
#     raw_command = input()
#
# print(f"Cupid's last position was {position}.")
# counter = 0
# for num in neighborhood:
#     if not num == 0:
#         counter += 1
#
# if counter == 0:
#     print(f"Mission was successful.")
# else:
#     print(f"Cupid has failed {counter} places.")


##########################################################################
def give_hearts(houses, house_index):
    houses[house_index] -= 2
    if houses[house_index] <= -2:
        print(f"Place {house_index} already had Valentine's day.")
    elif houses[house_index] <= 0:
        print(f"Place {house_index} has Valentine's day.")
    return houses


neighbours = [int(number) for number in input().split("@")]
cupid_position = 0

command = input().split()
while command[0] != "Love!":
    value = int(command[1])
    cupid_position += value
    if cupid_position >= len(neighbours):
        cupid_position = 0

    neighbours = give_hearts(neighbours, cupid_position)
    command = input().split()

print(f"Cupid's last position was {cupid_position}.")

failed_houses = [int(house) for house in neighbours if int(house) > 0]

if failed_houses:  # if failed exists - True
    print(f"Cupid has failed {len(failed_houses)} places.")

else:
    print("Mission was successful.")
