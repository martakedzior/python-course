# Utwórz plik na pulpicie zawierający listę ok. 20 cytatów. Każdy cytat powinen się znaleźć w nowej linii.
# Utwórz funkcję, która losuje i wyświetla w sposób ciekawy cytat na dziś. Np. można wyświetlić tak:
#
# Quote of the day is:
#
# **************************************
#            be or not to be?
# **************************************
#
#     zmodyfikuj plik źródłowy, tak aby użytkownik mógł podać własną nazwę pliku z cytatami
#     plik z cytatami powinen również zawierać informację o autorze, wyświetl cytat i pod spodem autora

import random

def read_quote_file():
    quotes_file = "C:/Users/Marta/Desktop/cytaty.txt"

    with open(quotes_file, 'r', encoding='utf-8') as file:
        quotes = file.readlines()

    return quotes

def select_quote_of_the_day(quotes):
    quote = random.choice(quotes)
    return quote

def quote_of_the_day(content):

    content = content.split('-')

    print("Quote of the day is:")
    print(" ")
    print("*" * 150, "\n")
    print(content[0].center(150))
    print(content[1].center(150))
    print("*" * 150)


quotes = read_quote_file()
quote = select_quote_of_the_day(quotes)
quote_of_the_day(quote)