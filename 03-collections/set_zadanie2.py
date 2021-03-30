# 2▹ Utwórz listę L_test = [1, 2, 3, 4],
# krotkę T_test = (1, 2, 3, 4) oraz set S_test = {1, 2, 3, 4}.
# Jakie metody dostępne dla typu list nie będą działać dla typów tuple i set?

L_test = [1, 2, 3, 4]
T_test = (1, 2, 3, 4)
S_test = {1, 2, 3, 4}


print(L_test[2])
L_test.append("4")
print(L_test)
L_test.pop()
print(L_test)


print(T_test.index())

