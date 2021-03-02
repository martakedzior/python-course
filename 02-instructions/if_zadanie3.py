#Stwórz skrypt, który przyjmuje 3 opinie użytkownika o książce. Oblicz średnią opinię o książce.
# W zależności od wyniku dodaj komunikaty. Jeśli uzytkownik ocenił książkę na ponad 7 - bardzo dobry,
# ocena 5-7 przeciętna, 4 i mniej - nie warta uwagi.

user_rating1 = int(input('Please provide rating nr 1 from 1 to 10: '))
user_rating2 = int(input('Please provide rating nr 2 from 1 to 10: '))
user_rating3 = int(input('Please provide rating nr 3 from 1 to 10: '))

average_book_rating = (user_rating1 + user_rating2 + user_rating3)/3

if average_book_rating >= 7:
    print("You have rated this book as VERY GOOD!")
elif average_book_rating >= 5:
    print("You have rated this book as AVERAGE")
else:
    print("Don't bother!")
