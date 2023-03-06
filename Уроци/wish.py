question_customers = input("Do you want to know the bestsellers: ").lower()

if question_customers == "yes":
    entered_category = input("Enter a category: ")
    if entered_category == "food":
        print("Milk 1l, Raisin cookies, Peaches")
    else:
        print("Laundry detergent, Shoe brush")
else:
    print("Let us know if you change your mind")