# Utwórz zmienną przechowującą dowolny ciąg znaków.
# Sprawdź czy utworzony string jest dłuższy niż 5 znaków oraz czy zawiera literę a.
# Jeśli zawiera, wszystkie litery a podmień na z i wyświetl powstały napis.

random_text = 'efaaaad3'
random_text_len = len(random_text)
lenght_correct = random_text_len > 5

if not lenght_correct:
    print('Hasło jest za krótkie, hasło musi mieć min. 5 znaków.')

for i in random_text:
    if i == 'a':
        random_text = random_text.replace('a','i')

print(random_text)
