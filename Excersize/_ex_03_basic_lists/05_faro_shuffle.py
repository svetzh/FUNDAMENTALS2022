# cards = input().split()
# number_of_shuffles = int(input())
#
# top_card = cards[0]
# bottom_card = cards[-1]
#
# half = len(cards) // 2
# shuffled_cards = []
# for n_shuffle in range(number_of_shuffles):
#     left_cards = []
#     right_cards = []
#
#     for index in range(1, half):
#         left_cards.append(cards[index])
#
#     for index in range(half, len(cards) - 1):
#         right_cards.append(cards[index])
#
#     for index in range(len(left_cards)):
#         shuffled_cards.append(right_cards[index])
#         shuffled_cards.append(left_cards[index])
#
#     cards = shuffled_cards.copy()
#     cards.append(bottom_card)
#     cards.insert(0, top_card)
#     shuffled_cards = []
#
# print(cards)

cards = input().split()
n = int(input())
half_size = len(cards) // 2

for i in range(n):
    left_side = cards[:half_size]
    right_side = cards[half_size:]  # second argument is omitted till the end

    faro_cards = []

    for element in range(len(left_side)):
        faro_cards.append(left_side[element])
        faro_cards.append(right_side[element])

    cards = faro_cards

print(cards)
