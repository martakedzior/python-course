# Rozwiązanie Rity

password = input('Podaj hasło: ')

password_len = len(password)
lenght_correct = password_len >= 8
includes_letters_and_digits = not password.isdigit() and not password.isalpha() and password.isalnum()
at_list_one_capital_letter = not password.islower()

if not lenght_correct:
    print('Hasło jest za krótkie, hasło musi mieć min. 8 znaków.')

if not includes_letters_and_digits:
    print('Hasło musi się składać z lilter i cyfr.')

if not at_list_one_capital_letter:
    print('Hasło musi zawierać co najmniej 1 dużą literę.')
