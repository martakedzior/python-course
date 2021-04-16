# Napisz program, który wyświetli kolejne wyniki dla silni liczby naturalnej N (N podane przez użytkownika, ale nie większe niż 8).
#
# Przykłady:
#     0! = 1
#     1! = 1
#     3! = 1⋅2⋅3 = 6
#     4! = 1⋅2⋅3⋅4 = 24
#     6! = 1⋅2⋅3⋅4⋅5⋅6 = 720
#
# Pamiętaj: nie pozwól użytkownikowi wprowadzić liczby, większej niż 8, wyświetl komunikat o błędzie.

user_input = int(input('Podaj wartość dla silni liczby naturalnej nie większej niż 8: '))

calculation = 1
for i in range(user_input+1):
    print(f'{i}!= {calculation}')
    calculation *= i + 1




