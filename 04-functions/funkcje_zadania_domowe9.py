# 9▹ Kolejnym warunkiem, aby dostać “żółte tablice”, jest to, aby samochód posiadał co najmniej 75% oryginalnych części.
# W naszym zadaniu zakładamy, że rzeczoznawca określił jego oryginalność w kategorii tak/nie.
#
#     Poniżej stworzenia i wyświetlenia słownika w zadaniu powyżej:
#             dopisz do słownika nowy klucz czy_oryginalny i ustaw jego wartość (typ: bool) wedle uznania.
#             ponownie wyświetl zmieniony słownik
#
#     Zmodyfikuj program tak, aby uwzględnił decyzję o możliwości zarejestrowania samochodu również od jego oryginalności.
#     Dopisz odpowiednie komunikaty.


def is_this_car_old_enough(car):
    if 2021 - car['year'] >= 25 and car['is_original'] == True:
        print(f'Gratulacje! Twój samochód {car["brand"]} może być zarejestrowany jako zabytek.')
    elif 2021 - car['year'] >= 25 and car['is_original'] == False:
        print(f'Twój samochód {car["brand"]} ma więcej niż 25 lat ale nie ma oryginalnych części i nie może być zarejestrowany jako zabytek.')
    else:
        print(f'Twój samochód {car["brand"]} jest jeszcze zbyt młody.')



# main program

car = {
    'brand': 'renault',
    'model': 'megan',
    'year': 1990,
    'is_original': False
}

print(car)

is_this_car_old_enough(car)
