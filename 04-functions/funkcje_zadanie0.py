#1. Napisz funkcję, ktra pyta użytkownika o pary książka + ocena i zapisuje je w programie.


def book_rating():
    book = input('Please provide name of the book to rate: ')
    rating = input('Please provide book rating in range from 1 to 5: ')
    books_with_ratings = []
    books_with_ratings.append(book + " " + rating)

book_rating()

