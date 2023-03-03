number = int(input())

for i in range(number):
    message = int(input())
    if message == 88:
        print('Hello')
        continue
    if message == 86:
        print('How are you?')
        continue
    if message < 88:
        print("GREAT!")
        continue
    if message > 88:
        print("Bye.")
        continue
