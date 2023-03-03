# lost_fights_count = int(input())
#
# helmet_price = float(input())
# sword_price = float(input())
# shield_price = float(input())
# armor_price = float(input())
#
# total_broken_helms = lost_fights_count // 2
# total_broken_sword = lost_fights_count // 3
# total_broken_shield = lost_fights_count // 6
# total_broken_armor = lost_fights_count // 12
#
# expenses = total_broken_helms * helmet_price + \
#            total_broken_sword * sword_price + \
#            total_broken_shield * shield_price + \
#            total_broken_armor * armor_price
#
# print(f"Gladiator expenses: {expenses:.2f} aureus")

arr = [1, 2, 3]
print(*arr, sep=", ")