# Utwórz klasę Customer, która ma pola imię nazwisko, oraz email klienta
# Dodaj metodę rejestracji, która zwraca datę o tyle dni do przodu ile customer ma liter w imieniu i nazwisku

import datetime as t

class Customer:
    def __init__(self, name, surname, client_email):
        self.name = name
        self. surname = surname
        self.client_email = client_email

    def registration(self):
        number_of_days = len(self.name) + len(self.surname)
        today = t.datetime.today()
        registration_date = today + t.timedelta(number_of_days)
        return registration_date.strftime('%Y-%m-%d')


if __name__ == "__main__":
    osoba = Customer("Maciej", "Kowalski", "maciejkowalski@com.pl")
    print(osoba.registration())