# Zapytaj użytkownika o numer od 1 do 100, jeśli użytkownik zgadnie liczbę ukrytą przez
# programistę wyświetl komunikat “gratulacje!”, w przeciwnym razie wyświetl “pudło!”.

user_input = int(input('Podaj proszę liczbę naturalną od 1 do 100: '))
dev_hidden_number = 55

if user_input == dev_hidden_number:
    print("gratulacje!")
else:
    print("pudło!")