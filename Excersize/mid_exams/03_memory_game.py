# def check_index_is_valid(index, len_list):
#     if index in range(len_list):
#         return True
#     return False
#
#
# cards = input().split()
# command = input()
# rounds_counter = 0
#
# while not command == "end" and cards:
#     index1, index2 = command.split()
#     index1 = int(index1)
#     index2 = int(index2)
#
#     rounds_counter += 1
#
#     if check_index_is_valid(index1, len(cards)) \
#             and check_index_is_valid(index2, len(cards)) \
#             and index1 != index2:
#         el_1 = cards[index1]
#         el_2 = cards[index2]
#         if el_1 == el_2:
#             cards.remove(el_1)
#             cards.remove(el_2)
#             print(f"Congrats! You have found matching elements - {el_1}!")
#         else:
#             print("Try again!")
#     else:
#         element_to_add = f"-{rounds_counter}a"
#         middle = len(cards) // 2
#         cards.insert(middle, element_to_add)
#         cards.insert(middle, element_to_add)
#         print("Invalid input! Adding additional elements to the board")
#
#     command = input()
#
# if not cards:
#     print(f"You have won in {rounds_counter} turns!")
# else:
#     print("Sorry you lose :(")
#     print(" ".join(cards))
###################################################################################
# def is_index_in_range(index, cards_count):
#     if 0 <= index < cards_count:
#         return True
#     return False
#
#
# def check_indices_are_valid(index1, index2, count_cards):
#     if is_index_in_range(index1, count_cards) and\
#             is_index_in_range(index2, count_cards):
#         return True
#     return False
#
#
# cards = input().split()
# n_moves = 0
# command = input()
# while command != "end":
#     n_moves += 1
#     index1, index2 = [int(el) for el in command.split()]
#
#     if check_indices_are_valid(index1, index2, len(cards)):
#         if cards[index1] == cards[index2]:
#             element = cards[index1]
#             cards.pop(index1)
#             # Elements are reordered after pop so we need to use the .remove,
#             # because the indexes are no longer accurate
#             cards.remove(element)
#             print(f"Congrats! You have found matching elements - ${element}")
#         else:
#             print("Try again!")
#     else:
#         element_to_add = f"-{n_moves}a"
#         index = len(cards) // 2
#         cards.insert(index, element_to_add)
#         cards.insert(index, element_to_add)
#         print(f"Invalid input! Adding additional elements to the board")
#     if not cards:
#         print(f"You have won in {n_moves} turns!")
#         exit(0)
#
#     command = input()
# print("Sorry you lose :(")
# print(*cards, sep=" ")

###################################################################################

def is_valid_index(index, list_length):
    return 0 <= index < list_length


items = input().split()
command_input = input()
moves_counter = 0
is_won = False

while command_input != "end":
    command_args = command_input.split()
    index_one = int(command_args[0])
    index_two = int(command_args[1])
    moves_counter += 1

    if index_one == index_two \
            or not is_valid_index(index_one, len(items)) \
            or not is_valid_index(index_two, len(items)):
        new_item = f"-{moves_counter}a"
        middle_index = len(items) // 2
        items.insert(middle_index, new_item)
        items.insert(middle_index, new_item)
        print("Invalid input! Adding additional elements to the board")

        command_input = input()
        continue
    if items[index_one] != items[index_two]:
        print("Try again!")
        command_input = input()
        continue

    removed_item = items.pop(index_one)
    items.remove(removed_item)
    print(f"Congrats! You have found matching elements - {removed_item}!")

    if len(items) == 0:
        is_won = True
        break

    command_input = input()

if is_won:
    print(f"You have won in {moves_counter} turns!")
else:
    print("Sorry you lose :(")
    print(" ".join(items))










