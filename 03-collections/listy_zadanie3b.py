# 3▹ Dla podanej przez użytkownika liście liczb całkowitych sprawdź czy pierwszy i ostatni element są takie same.

numbers = input('Podaj liczby po przecinku: ')
numbers = numbers.split(',')
print(numbers)

print('Czy pierwsza i ostatnia liczba są takie same:', numbers[0] == numbers[-1])

