# Zadanie 7
# Napisz konwerter walut.
# Program poprosi użytkownika o kwotę pieniędzy, jaką wezmą na wakacje
# a następnie przeliczy tę kwotę w euro oraz w dolarach.
# Zignoruj wszelkie centy, które mogą wyniknąć z konwersji.
# Wejście i wyjście powinny być zrozumiałe dla użytkownika.

amount_of_money_PLN = int(input('Please provide amount of money you will take with you to your vacation in PLN: '))
amount_of_money_EUR = amount_of_money_PLN / 4.50
amount_of_money_DOL = amount_of_money_PLN / 3.75

print(f'You will take: {amount_of_money_PLN} PLN that will allow you to buy: {round(amount_of_money_EUR)} EUR or {round(amount_of_money_DOL)} DOL')

