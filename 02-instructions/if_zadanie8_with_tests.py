# Sortowanie. Trzy dowolne liczby podane przez użytkownika zapisz do trzech zmiennych.
# Znajdź największą liczbę. Wyświetl liczby od największej do najmniejszej.

#print('Podaj proszę trzy dowolne liczby. Posortuje je od największej do najmniejszej.')
# user_input1 = float(input('Podaj pierwszą liczbę: '))
# user_input2 = float(input('Podaj pierwszą liczbę: '))
# user_input3 = float(input('Podaj pierwszą liczbę: '))

def equals(actual, expected):
    assert actual == expected, f'Expected {expected}, got {actual}'

def max_from_three(user_input1, user_input2, user_input3):
    max_number = 0
    if user_input1 > user_input2:
        max_number = user_input1
    elif user_input2 > user_input3:
        max_number = user_input2
    elif user_input3 > max_number:
        max_number = user_input3

    return max_number


equals(max_from_three(2, 34, 56), 56)
equals(max_from_three(200, 34, 56), 200)
equals(max_from_three(2, 340, 56), 340)



