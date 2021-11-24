book_name = input()
found_book = False
total_books_count = 0

while book_name != "No More Books":
    current_book_name = input()
    if current_book_name == book_name:
        found_book = True
        break
    elif current_book_name == "No More Books":
        break
    total_books_count += 1


if found_book == True:
    print(f'You checked {total_books_count} books and found it.')
else:
    print('The book you search is not here!')
    print(f'You checked {total_books_count} books.')

