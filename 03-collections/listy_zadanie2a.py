# 2▹ Pobierz od użytkownika 10 liczb, wyświetl tylko te, które są nieparzyste.

print('Podaj proszę 10 liczb całkowitych: ')

user_list = []

for i in range(10):
    user_input = input('Podaj liczbę całkowitą: ')
    user_list.append(user_input)

print('Wśród podanych liczb następujące liczby są liczbami nieparzystymi: ')

for liczba in user_list:
    if int(liczba) % 2 != 0:
        print(liczba, end=', ')
