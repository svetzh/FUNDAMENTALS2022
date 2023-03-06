num = int(input())

opened_count = 0
closing_count = 0
is_balanced = True
opened = "("
closed = ")"
random_str = ''

for i in range(num):
    some_str = input()

    if some_str == opened:
        opened_count += 1
    elif some_str == closed:
        closing_count += 1

    if closing_count > opened_count:
        is_balanced = False
        break
    elif opened_count - 1 > closing_count:
        is_balanced = False
        break
if is_balanced:
    print("BALANCED")
else:
    print("UNBALANCED")