# 5▹ Utwórz “na sztywno” 2-wymiarową tablicę, tak, by kolejne wiersze zawierały dane osób,
#  natomiast w kolumnach będzie znajdować się imię, nazwisko, zawód, np:
#
#     Dorota, Wellman, dziennikarka
#
#     Adam, Małysz, sportowiec
#
#     Robert, Lewandowski, piłkarz
#
#     Krystyna, Janda, aktorka
#
# Wyświetl w sposób przyjazny dla użytkownika

two_dimension_table = [
    ['Dorota', 'Wellman', 'dziennikarka'],
    ['Adam', 'Małysz', 'sportowiec'],
    ['Robert', 'Lewandowski', 'piłkarz'],
    ['Krystyna', 'Janda', 'aktorka'],
]

print(two_dimension_table)

for element in two_dimension_table:
    print(', '.join(element))