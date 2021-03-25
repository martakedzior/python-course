# Utwórz plik na pulpicie zawierający listę ok. 20 cytatów. Każdy cytat powinen się znaleźć w nowej linii.
# Utwórz funkcję, która losuje i wyświetla w sposób ciekawy cytat na dziś. Np. można wyświetlić tak:
#
# Quote of the day is:
#
# **************************************
#            be or not to be?
# **************************************
#
#     zmodyfikuj plik źródłowy, tak aby użytkownik mógł podać własną nazwę pliku z cytatami
#     plik z cytatami powinen również zawierać informację o autorze, wyświetl cytat i pod spodem autora

from random import randrange

filename = "C:/Users/Henrik Kiepe/Desktop/citates.txt"

with open(filename, 'r') as fopen:
    lines = fopen.readlines()



print("Quote of the day is:")
print("**************************************")
print(lines[randrange(len(lines)) - 1])
print("**************************************")

