# 3▹ Dla podanej przez użytkownika liście liczb całkowitych sprawdź czy pierwszy i ostatni element są takie same.

# user_input = [4, 3, 6, 7, 3, 4]
user_input = []
user_input = input('podaj liczby przedzielone spacjami: ')
print(user_input)

if user_input[0] == user_input[-1]:
    print("takie same")
else:
    print("nie takie same")