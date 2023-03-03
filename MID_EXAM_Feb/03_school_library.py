shelf_books = input().split("&")
command = input()
while command != "Done":
    command_args = command.split(" | ")
    action = command_args[0]
    book_name = command_args[1]
    if action == "Add Book":
        if book_name not in shelf_books:
            shelf_books.insert(0, book_name)

    elif action == "Take Book":
        if book_name in shelf_books:
            shelf_books.remove(book_name)

    elif action == "Swap Books":
        book1 = command_args[1]
        book2 = command_args[2]
        if book1 in shelf_books and book2 in shelf_books:
            first_ix = shelf_books.index(book1)
            second_ix = shelf_books.index(book2)
            shelf_books[first_ix], shelf_books[second_ix] = shelf_books[second_ix], shelf_books[first_ix]
        # if book_name not in shelf_books:
        #     command = input()
        #     continue
        # else:
        #     book_idx1 = shelf_books.index(book_name)
        #     book_idx2 = shelf_books.index(command_args[2])
        #     if book_idx1 in shelf_books and book_idx2 in shelf_books:
        #         shelf_books[book_idx1], shelf_books[book_idx2] = shelf_books[book_idx2], shelf_books[book_idx1]

    elif action == "Insert Book":
        if book_name not in shelf_books:
            shelf_books.append(book_name)

    elif action == "Check Book":
        if 0 <= int(book_name) < len(shelf_books):
            print(shelf_books[int(book_name)])

    command = input()
# print(*shelf_books, sep=", ")
print(", ".join(shelf_books))

