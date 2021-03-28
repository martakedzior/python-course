# 4▹ Wyświetl 3 losowe cytaty

from random import choice


def select_quote(quotes):
    quote = choice(quotes)
    return quote


def reformat(quote):
    quote_and_author = quote.split(' - ')
    return quote_and_author


def show(quote):
    print(quote[0].center(50))
    print(quote[1].strip().center(50))


def show_first_5(quotes):
    for q in quotes[0:5]:
        print(q)


# Main program
filename = "quotes.txt"
with open(filename, 'r', encoding='utf-8') as fopen:
    lines = fopen.readlines()

for i in range(0, 3):
    quote = select_quote(lines)
    quote = reformat(quote)
    show(quote)
    i += 1
