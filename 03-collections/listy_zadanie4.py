# 4▹ Pobierz od użytkownika parzystą listę elementów. Sprawdź czy 2 środkowe elementy są takie same.


print('Podaj proszę parzystą liczbę elementów.: ')

user_list = []

for i in range(10):
    user_input = input('Podaj liczbę całkowitą: ')
    user_list.append(user_input)

print('Wśród podanych liczb następujące liczby są liczbami nieparzystymi: ')

for liczba in user_list:
    if int(liczba) % 2 != 0:
        print(liczba, end=', ')