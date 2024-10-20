# TODO Найдите количество книг, которое можно разместить на дискете

size_of_book_in_bytes = 100 * 50 * 25 * 4
numbers_of_books = (1.44 * 1024 * 1024) // size_of_book_in_bytes
numbers_of_books = round(numbers_of_books)

print("Количество книг, помещающихся на дискету:", numbers_of_books)
