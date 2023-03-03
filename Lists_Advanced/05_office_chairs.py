number_rooms = int(input())
are_chairs_enough = True
free_chairs = 0

for room in range(1, number_rooms + 1):
    chairs, visitors = input().split()
    visitors = int(visitors)
    diff = abs(len(chairs) - visitors)
    if len(chairs) < visitors:
        print(f"{diff} more chairs needed in room {room}")
        are_chairs_enough = False
    else:
        free_chairs += diff

if are_chairs_enough:
    print(f"Game On, {free_chairs} free chairs left")

