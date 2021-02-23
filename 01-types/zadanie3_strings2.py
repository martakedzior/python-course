# 1. Stwórz zmienną przechowującą wyraz o długości nieparzystej większej niż 7 i zwróć łańcuch złożony z trzech środkowych znaków danego ciągu.


text = 'przetrwalnik'

middle = int(len(text) // 2)
print(text[middle - 1 : middle + 2])