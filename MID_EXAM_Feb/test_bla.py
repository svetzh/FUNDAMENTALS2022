# shelf_books = input().split("&")
# command = input()
# while command != "Done":
#     command_args = command.split(" | ")
#     action = command_args[0]
#     book_name = command_args[1]
#     if action == "Swap Books":
#         book_one = shelf_books.index(command_args[1])
#         book_two = shelf_books.index(command_args[2])
#         book_name_2 = command_args[2]
#         if book_name in shelf_books and book_name_2 in shelf_books:
#             shelf_books = []

shelf_books = input().split("&")
command = input()
while command != "Done":
    command_args = command.split(" | ")
    action = command_args[0]

    if action == "Add Book":
        book_name = command_args[1]
        if book_name not in shelf_books:
            shelf_books.insert(0, book_name)
    elif action == "Take Book":
        book_name = command_args[1]
        if book_name in shelf_books:
            shelf_books.remove(book_name)
    elif action == "Swap Books":
        book_name = command_args[1]
        book_name2 = command_args[2]
        book_one = shelf_books.index(command_args[1])
        book_two = shelf_books.index(command_args[2])
        if book_name in shelf_books and book_name2 in shelf_books:
            shelf_books[book_one], shelf_books[book_two] = \
                shelf_books[book_two], shelf_books[book_one]

    elif action == "Insert Book":
        book_name = command_args[1]
        if book_name not in shelf_books:
            shelf_books.append(book_name)

    elif action == "Check Book":
        book_name = command_args[1]
        idx = int(book_name)
        if idx in range(len(shelf_books) - 1):
            print(shelf_books[idx])

    command = input()
print(", ".join(shelf_books))