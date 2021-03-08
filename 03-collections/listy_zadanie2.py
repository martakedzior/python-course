# 2▹ Pobierz od użytkownika 10 liczb, wyświetl tylko te, które są nieparzyste.

user_input = []
user_input = input('Podaj proszę 10 liczb całkowitych oddzielonych przecinkiem: ')

user_input = user_input.split(',')

print('Wśród podanych liczb następujące są liczbami nieparzystymi: ')

for liczba in user_input:
    if int(liczba) % 2 != 0:
        print(liczba, end=', ')
