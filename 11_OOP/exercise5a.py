from abc import ABC, abstractmethod


class Vehicle(ABC):
    property(license)

    @abstractmethod
    def description(self):
        pass


class Car(Vehicle):
    license = 'B'

    def description(self):
        print("I've got 4 wheels and i cant weight over 3,5 tonnes")


class Bike(Vehicle):
    license = 'None'

    def description(self):
        print("I've got 2 wheels and a pedals!")


class Bus(Vehicle):
    license = 'D or D/E or D1 or D1+E'

    def description(self):
        print("I've got 4 wheels and can take more than 7 passengers!")


class Truck(Vehicle):
    license = 'C or C+E'

    def description(self):
        print("I've got 4 or 6 wheels and can take a lot of cargo!")


BMW = Car()
BMW.description()
print(f"You need license of {BMW.license} category to drive me")