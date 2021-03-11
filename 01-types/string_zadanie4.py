# 4. Utwórz skrypt, który zapyta użytkownika o tytuł książki, nazwisko autora, liczbę stron, a następnie:
# Sprawdź czy tytuł i nazwisko składają się tylko z liter, natomiast liczba stron jest wartością liczbową.
# Użytkownicy bywają leniwi. Nie zawsze zapisują tytuły i nazwisko z dużej litery – popraw ich
# Połącz dane w jeden ciąg book za pomocą spacji
# Policz liczbę wszystkich znaków w napisie book

# ******* rozwiązanie zadania wymaga jeszcze podszlifowania *********

print('Podaj proszę następujące informacje o książkach: ')

book_title = input('Podaj proszę tytuł książki: ')
authors_name = input('Podaj nazwisko autora tej książki: ')
page_number = input('Podaj liczbę stron tej książki: ')

book_title = book_title[0].upper() + book_title[1:]
authors_name = authors_name[0].upper() + authors_name[1:]

if book_title.isalpha() == True:
    print(f'Tytuł {book_title} jest poprawnym tytułem książki.')
else:
    print('Tytuł książki zawiera liczby.')

if authors_name.isalpha() == True:
    print(f'Nazwisko autora: {authors_name} zawiera tylko znaki alfabetu.')
else:
    print('Podane nazwisko autora zawiera liczby.')

if page_number.isdigit() == True:
    print('Poprawnie podana liczba stron')
else:
    print('Podana liczba stron nie jest wyrażona liczbowo.')

spacja = " "
book = book_title + spacja + authors_name + spacja + page_number

print(book)

