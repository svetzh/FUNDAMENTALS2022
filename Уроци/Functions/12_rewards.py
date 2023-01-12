# calc number of points
def total_grade(number_subjects):
    sum_points = 0
    for subject in range(number_subjects):
        points = int(input("Enter grade:"))
        sum_points += points
    return sum_points

# choosing and printing appropriate award
def issuing_cert(number_subjects):
    total_score = total_grade(number_subjects)  # when we call the 1st function into 2nd function. Creating variable
    if total_score > 80:
        return "Award with a diploma"
    elif total_score > 50:
        return "Award of cert of commendation"
    else:
        return "Cert of participation"


enter_name = input("Enter your name or STOP: ")
while enter_name.upper() != "STOP":
    number_subjects = int(input("Enter your number of subjects: "))
    print(f"Total score: {total_grade(number_subjects)}")
    print(f"{issuing_cert(number_subjects)}")

    enter_name = input("Enter your name or STOP: ")
