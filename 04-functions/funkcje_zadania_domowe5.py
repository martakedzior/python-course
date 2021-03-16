# 5▹ Napisz grę ciepło - zimno tak, aby korzystać z funkcji.

import random

def cold_warm_game():
    computer_pick = random.randint(1, 100)
    counter = 6

    while counter > 0:
        user_guess = int(input('Zgadnij wylosowaną liczbę całkowitą: '))

        if computer_pick == user_guess:
            print(f'Zgadłeś. Komputer wylosował: {computer_pick}!')
            break
        elif abs(computer_pick - user_guess) > 20:
            print(f'Bardzo zimno! ')
        elif abs(computer_pick - user_guess) > 10:
            print(f'Zimno! ')
        elif abs(computer_pick - user_guess) > 5:
            print(f'Cieplej! ')
        elif abs(computer_pick - user_guess) > 3:
            print(f'Bardzo ciepło! ')
        else:
            print(f'Bardzo bardzo ciepło!')

        counter -= 1
        if counter == 0:
            print(f'Skończyły Ci się próby. Komputer wylosował liczbę: {computer_pick}')


cold_warm_game()