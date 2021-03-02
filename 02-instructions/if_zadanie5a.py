# Stwórz zmienną password. Hasło powinno składać z liter i cyfr, zwierać conajmniej 1 dużą literę i mieć długość conajmniej 8 znaków.
# Poinformuj użytkownika, jeśli wpisane hasło jest nie poprawne. Wyświetl różne komunikaty w zależności od rodzaju błędu.

password = input("Stwórz hasło, które składa się z liter i cyfr, ma długośc conajmniej 8 znaków oraz conajmniej 1 dużą literę: ")
if len(password) < 8:
    print("Twoje hasło jest za krótkie!")
elif password.isalpha():
    print("Twoje hasło nie zawiera żadnej cyfry!")
elif password.isdigit():
    print("Twoje hasło nie zawiera żadnej litery!")
elif password.islower():
    print("Twoje hasło nie ma żadnej dużej litery!")
else:
    print("Hasło poprawnie utworzone!")

