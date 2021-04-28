#5. 5▹ Stwórz abstrakcyjną klasę Pojazdy. Utwórz potomne klasy pojazdy np. Samochód, Rower, Autobus, Ciężarówki.
# Dodaj opisy zgodne z tym jak te pojazdy są klasyfikowane. Jaki rodzaj dokumentu jest potrzebny, by kierować poszczegolnym pojazdem.

from abc import ABC, abstractmethod


class Vehicles(ABC):
    @abstractmethod
    def licence(self):
        pass


class Bicycle(Vehicles):
    def licence(self):
        print("To drive car you need cycling card only!")


class Car(Vehicles):
    def licence(self):
        print("To drive car you need driving licence B1!")


class Bus(Vehicles):
    def licence(self):
        print("To drive car you need driving licence C1!")


class Tir(Vehicles):
    def licence(self):
        print("To drive car you need driving licence ****!")


if __name__ == "__main__":
    ktm = Bicycle()
    ktm.licence()

    peugeot = Car()
    peugeot.licence()

    big_bus = Bus()
    big_bus.licence()

    tir = Tir()
    tir.licence()

