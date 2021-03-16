# 4▹ Napisz grę - kamień (k) / papier (p) / nożyce (n).
#
#         Użytkownik podaje jedną z 3 figur.
#         Komputer losuje jedną z 3 figur.
#         Sprawdź kto wygrał tę rundę.
#         Zmień kod tak, by użytkownik mógł podac liczbę rund.
#         Wygrana jest podawana jako suma wygranych rund komputer vs użytkownik.
#
#         Zmień tak, by gracz mógł zakończyć grę w dowolnej chwili przez np. hasło ‘koniec’
#
#         Zasady:
#         - Nożyce biją papier
#         - Papier bije kamień
#         - Kamień bije nożyce

import random

game_options = ['k', 'p', 'n']

print('Witaj w grze w nożyce, papier, kamień! ')
game_counter = int(input('Ile rund chcesz rozegrać z komputerem? Podaj liczbę: '))

user_wins = 0
computer_wins = 0

while game_counter > 0:
    user_choice = input('Podaj kamień (k) /papier(p)/ nożyce(n): ')
    computer = random.choice(game_options)

    if user_choice == computer:
        print('Remis')
    elif user_choice == 'n' and computer == 'p':
        print(f'Nożyce ({user_choice}) biją papier ({computer}). Wygrałeś!')
        user_wins += 1
    elif user_choice == 'p' and computer == 'k':
        print(f'Papier ({user_choice}) bije kamień ({computer}). Wygrałeś!')
        user_wins += 1
    elif user_choice == 'k' and computer == 'n':
        print(f'Kamień ({user_choice}) bije nożyce ({computer}). Wygrałeś!')
        user_wins += 1
    elif computer == 'n' and user_choice == 'p':
        print(f'Przegrałeś! Nożyce ({computer}) biją papier ({user_choice}).')
        computer_wins += 1
    elif computer == 'p' and user_choice == 'k':
        print(f'Przegrałeś! Papier ({computer}) bije kamień ({user_choice}).')
        computer_wins += 1
    elif computer == 'k' and user_choice == 'n':
        print(f'Przegrałeś! Kamień ({computer}) bije nożyce ({user_choice}).')
        computer_wins += 1

    game_counter -= 1
    if game_counter == 0 and user_wins > computer_wins:
        print(f'Wygrałeś z komputerem {user_wins} do {computer_wins}!')
    elif game_counter == 0 and computer_wins > user_wins:
        print(f'Przegrałeś z komputerem {computer_wins} do {user_wins}!')
    elif game_counter == 0 and user_wins == computer_wins:
        print(f'Remis: {user_wins}:{computer_wins}!')

    if user_choice == 'koniec':
        print('Dziękuję za wspólną grę!')
        break
