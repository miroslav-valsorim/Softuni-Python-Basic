book_wanted = input()
books_checked = input()

total_books_checked = 0

while books_checked != book_wanted:
    total_books_checked += 1

    if books_checked == "No More Books":
        print(f"The book you search is not here!")
        print(f"You checked {total_books_checked - 1} books.")
        break

    books_checked = input()

else:
    print(f"You checked {total_books_checked} books and found it.")
