# 1. Napisz funkcję, ktra pyta użytkownika o pary książka + ocena i zapisuje je w programie.
# 2. Napisz funkcję, która zapyta o numer książki i wyświetli film wraz z oceną.
# 3. W prosty sposób obsłuż błąd użytkownika - użytkownik zapyta o numer w bazie, który nie istnieje.

def get_books():
    counter = int(input('How many books you would like to add? '))

    books_collection = []
    for book in range(counter):
        title = input('Book title: ')
        rate = int(input(f'{title} - rate [0-10]: '))
        books_collection.append([title, rate])

    return books_collection

def show_rate(books_list):
    nr = int(input('Which book you want to see? (Give me a number): '))
    index = nr - 1

    if nr > len(books_list) or nr < 0:
        print('No such book in collection')
    else:
        print(f'Book {books_list[index][0]} is rated -> {books_list[index][1]}')


#------main part ------
print('Welcome to my library! -------')
books = get_books()
print('Added!')

show_rate(books)