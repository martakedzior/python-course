# Utwórz dowolną tablicę n x n zawierającą dowolny znak, a następnie wyświetl jej elementy w formie tabeli n x n.
# Elementy powinny być oddzielone spacją

n = int(input('Give me number of row and columns N='))

tab = [['-'] * n ] * n


print(tab)

for row in tab:
    print(' '.join(row))