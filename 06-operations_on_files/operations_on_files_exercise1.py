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
        print(quotes)
    return quotes

def quote_of_the_day(content):

    content = str(random.choice(content)).center(150)

    print("Quote of the day is:")
    print(" ")
    print("*" * 150, "\n")
    print(content)
    print("*" * 150)

quotes = read_quote_file()
quote_of_the_day(quotes)