fav_book = input()
current_book = input()
book_is_found = True
counter = 0

while current_book != fav_book:
    if current_book != "No More Books":
        counter += 1
    else:
        book_is_found = False
        break
    current_book = input()

if book_is_found:
    print(f"You checked {counter} books and found it.")
else:
    print("The book you search is not here!")
    print(f"You checked {counter} books.")