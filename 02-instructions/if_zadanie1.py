#Poproś użytkownika o podanie liczby.
# Sprawdź czy liczba podana przez użytkownika jest podzielna przez 3 bez reszty i wyświetl komunikat
# “Twoja liczba jest podzielna przez 3”.


user_number = int(input('Please provide a number: '))

if user_number % 3 == 0:
    print("Your number is divided by 3.")
else:
    print("Your number is not divided by 3.")

#print("Your number is divided by 3.") if user_number % 3 ==0 else print("Your number is not divided by 3.")
