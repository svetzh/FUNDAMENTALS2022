def get_result(score):
    if score >= 85:
        return "1st place"
    elif 65 <= score < 85:
        return "2nd place"
    elif 50 <= score < 65:
        return "3rd place"
    else:
        return "Better luck next time!"


def give_result(result):
    if result == "1st place":
        return "Trip to St. Petersburg"
    elif result == "2nd place":
        return "Bookstore gift cert"
    elif result == "3rd place":
        return "Board game"
    else:
        return "Cert of participation"


score = int(input("Enter score: "))
result = get_result(score)
rewards = give_result(result)

print(f"Your result: {result} - {rewards}")
