# resources = {}
# while True:
#     line = input()
#     if line == "stop":
#         break
#
#     quantity = int(input())
#
#     if line in resources:
#         resources[line] += quantity
#     elif line not in resources:
#         resources[line] = quantity
#
# for line, quantity in resources.items():
#     print(f"{line} -> {quantity}")

# # 2 решение:

precious_metals = {}
command = input()
while command != "stop":
    quantity = int(input())

    if command not in precious_metals:
        precious_metals[command] = quantity
    else:
        precious_metals[command] += quantity

    command = input()

# # NORMAL FOR LOOP:
# for command, quantity in precious_metals.items():
#     print(f"{command} -> {quantity}")

# # WITH COMPREHENSION:
results = [f"{command} -> {quantity}" for command, quantity in precious_metals.items()]
print("\n".join(results))
