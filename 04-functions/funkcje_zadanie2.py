# 2▹ Napisać funkcję, która sprawdza czy liczba jest parzysta.

def check_if_even_number():
    user_number = int(input('Podaj liczbę całkowitą: '))
    if user_number % 2 == 0:
        print('Liczba parzysta')
    else:
        print('Liczba nieparzysta')


check_if_even_number()

