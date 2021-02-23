# Zadanie 5
# Napisz program, który pyta użytkownika o 2 liczby
# a następnie dzieli jedna przez drugą.
# Pokaż ile razy pierwsza liczba mieści się w drugiej
# oraz jaka jest reszta tego dzielenia. 

print("Podaj proszę 2 liczby: ")
print()

user_input1 = int(input("Pierwsza liczba: "))
user_input2 = int(input("Druga liczba: "))

result = user_input1 // user_input2
modulo = user_input1 % user_input2

print(f"Pierwsza liczba mieści się w drugiej: {result} razy.")
print(f"Reszta dzielenia pierwszej liczby przez drugą to: {modulo}.")