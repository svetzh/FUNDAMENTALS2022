def count_fives():
    grade = int(input("Enter grade: "))
    count_number = 0
    while grade != 0:
        if grade == 5:
            count_number += 1

        grade = int(input("Enter grade: "))
    return count_number


def give_discount():
    discount = count_fives()
    if discount >= 4 and discount <= 5:
        return 10
    elif discount > 5:
        return 15
    else:
        return 0


print(f"Discount on teather tickets (%): {give_discount()}")


