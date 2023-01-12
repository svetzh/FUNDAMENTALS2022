enter_category = input("Please enter category or 'stop' to end: ")

while enter_category != "stop":
    if enter_category == "meat":
        print("10% discount")
    elif enter_category == "drinks":
        print("30% discount")
    else:
        print("no discount")
    enter_category = input("Please enter category or 'stop' to end: ")
