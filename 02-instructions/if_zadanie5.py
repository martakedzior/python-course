# Stwórz zmienną password. Hasło powinno składać z liter i cyfr, zwierać conajmniej 1 dużą literę i mieć długość conajmniej 8 znaków.
# Poinformuj użytkownika, jeśli wpisane hasło jest nie poprawne. Wyświetl różne komunikaty w zależności od rodzaju błędu.



password = (input('Please provide your password: '))

if len(password) >= 8:
    if password.isdigit() != True:
        if password.islower() != True:
            print('Your password is correct')
        else:
            print('Your password should contain one big letter')
    else:
        print('Your password should contain letters and digits and have one big letter')
else:
    print('Your password should have 8 characters or more')
