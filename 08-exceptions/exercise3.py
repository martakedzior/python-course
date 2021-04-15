# 3▹ Stwórz listę 10 elementową (różne typy!). Pozwól użytkownikowi podać dowolny index.
# Podziel 1 przez liczbę pod indexem wybranym przez użytkownika. Obsłuż błędy.

items = [13, 'string', 2.45, 0, "e", True, False, [], {'key': 3}, ()]

index = len(items)
user_input = int(input(f'Please provide index from 1 to {index}: '))

try:
    result = 1 / items[user_input-1]
    print(result)
except (TypeError, ZeroDivisionError) as e:
    result = 0
    print(result, e)

