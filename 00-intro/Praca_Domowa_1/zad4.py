# Zadanie 4
# Napisz skrypt, który zapyta użytkownika o trzy liczby całkowite,
# a następnie pomnóż dwa pierwsze. przed podzieleniem wyniku przez trzecią liczbę. 
# Wejście i wyjście powinny być zrozumiałe dla użytkownika.

print("Podaj proszę 3 liczby całkowite")
print()

user_input1 = int(input("Pierwsza liczba: "))
user_input2 = int(input("Druga liczba: "))
user_input3 = int(input("Trzecia liczba: "))

result = round((user_input1 * user_input2) / user_input3, 2)

print(f"Wynik mnożenia dwóch pierwszych liczb podzielony przez trzecią liczbę to: {result}")
