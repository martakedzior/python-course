# Utwórz listę, która zawiera składniki na ulubione danie.
# Wyświetl komunikaty co należy po kolei dodać. Poza pętlą umieść pozostałe instrukcje
# np. “Wrzuć do piekarnika”, “Podawaj schłodzone”.

favourite_dish = ['marchewka', 'pomidory', 'makaron', 'cebula', 'mięso mielone', 'przyprawy']

for item in favourite_dish:
    print(f'Wrzuć: {item}')
    print('Zamieszaj')

print('Posyp parmezanem')