# 2. Stwórz dwie zmienne s1 i s2 przechowujące dowolne wyrazy, utwórz nowy łańcuch s3, dołączając s2 w środku s1.

s1 = 'random'
s2 = 'word'

middle_s1 = int(len(s1) // 2)

s3 = s1[0 : middle_s1] + s2 + s1[middle_s1 : len(s1)]

print(s3)

