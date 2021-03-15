# 4▹ Napisać funkcję, która wypisze wszystkie parzyste z przekazanej listy elementów (wykorzystać funkcje z zadania 2)


def check_if_even_number():
    counter = int(input('Ile liczb chcesz podać? '))

    user_list_of_numbers = []

    for i in range(counter):
        user_input = int(input('Podaj liczbę całkowitą: '))
        user_list_of_numbers.append(user_input)

    print('Wśród podanych liczb następujące liczby są liczbami parzystymi: ')

    for number in user_list_of_numbers:
        if number % 2 == 0:
            print(number, end=', ')  #a jak usunąć ten ostatni przecinek??


check_if_even_number()

