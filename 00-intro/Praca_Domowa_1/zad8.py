# Zadanie 8
# Ulepsz program z zadania 7, tak aby zwrócił ile banknotów
# 50, 20, 10 i 5 euro otrzyma użytkownik.


amount_of_money_PLN = int(input('Please provide amount of money you will take with you to your vacation in PLN: '))
amount_of_money_EUR = amount_of_money_PLN / 4.50
amount_of_money_USD = amount_of_money_PLN / 3.75

print(f'You will take: {amount_of_money_PLN} PLN that will allow you to buy: {round(amount_of_money_EUR)} EUR or {round(amount_of_money_USD)} USD')

notes_50_EUR = round(amount_of_money_EUR // 50)
notes_20_EUR = round(amount_of_money_EUR // 20)
notes_10_EUR = round(amount_of_money_EUR // 10)
notes_5_EUR = round(amount_of_money_EUR // 5)

notes_50_USD = round(amount_of_money_USD // 50)
notes_20_USD = round(amount_of_money_USD // 20)
notes_10_USD = round(amount_of_money_USD // 10)
notes_5_USD = round(amount_of_money_USD // 5)

print(f'You will receive {notes_50_EUR} notes of 50 EUR, {notes_20_EUR} notes of 20 EUR, {notes_10_EUR} notes of 10 EUR and {notes_5_EUR} of 5 EUR')
print(f'You will receive {notes_50_USD} notes of 50 USD, {notes_20_USD} notes of 20 USD, {notes_10_USD} notes of 10 USD and {notes_5_USD} of 5 USD')