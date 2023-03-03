party_size = int(input())
days = int(input())

total_coins = 0

for day in range(1, days + 1):
    if day % 10 == 0:
        party_size -= 2
    if day % 15 == 0:
        party_size += 5
    total_coins += 50 - (party_size * 2)
    if day % 3 == 0:
        total_coins -= party_size * 3
    if day % 5 == 0:
        total_coins += party_size * 20
        if day % 3 == 0:
            total_coins -= party_size * 2
print(f"{party_size} companions received {total_coins // party_size} coins each.")
