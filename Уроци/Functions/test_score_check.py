def score_check(score):
    if score >= 80:
        return True
    else:
        return False


participants = int(input("Enter the number of participants: "))

for student in range(participants):
    name = input("Enter your name: ")
    score = int(input("Enter test score: "))
    result = score_check(score)
    print(f"admitted: {result}")
