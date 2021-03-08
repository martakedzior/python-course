# 3▹ Utwórz 2 krotki.
# Następnie utwórz listę będącą połączeniem elementów o parzystym indeksie z pierwszej krotki,
# a oraz nieparzystych elementów z drugiej. Przekształć powstałą listę w set.


tuple_1 = (2, 3, 'hau', 'kijek')
tuple_2 = ('miau', 23, 300, 'lampa')

combine_list = []
counter_1 = len(tuple_1)
counter_2 = len(tuple_2)

for i in range(counter_1):
    if i % 2 == 0:
        print(i)
        combine_list.append(tuple_1[i])
        print(combine_list)

for a in range(counter_2):
    if a % 2 != 0:
        combine_list.append(tuple_2[a])
        print(combine_list)