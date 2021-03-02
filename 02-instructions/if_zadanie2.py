# Pobierz dwie liczby całkowite od użytkownika i oblicz ich sumę.
# Jeśli suma jest większa niż 100, wyświetl wynik, w przeciwnym wypadku wyświetl “Koniec”.

print('Podaj proszę dwie liczby całkowite.')
user_input1 = int(input('Podaj proszę pierwszą liczbę całkowitą: '))
user_input2 = int(input('Podaj proszę drugą liczbę całkowitą: '))

user_summ = user_input1 + user_input2

if user_summ >= 100:
    print(f"Suma wprowadzonych liczb to: {user_summ}")
else:
    print("Koniec")