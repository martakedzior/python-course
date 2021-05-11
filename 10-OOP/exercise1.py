# 1▹ Skorzystaj z wprowadzenia do OOP. Stwórz klasę Pies, która posiada wspomniane atrybuty oraz metodę.
#         atrybuty: imię, kolor sierści, rasę
#         metody: szczekaj, machaj ogonem
# Utwórz kilka obiektów klasy Pies z różnymi parametrami.


class Dog:
    def __init__(self, name, color, breed, age):      # initializer (w innych językach konstruktor)
        self.name = name
        self.color = color
        self.breed = breed
        self.age = age

    def bark(self):                             #metoda
        return self.name + " hau " * self.age

    def tail_wiggle(self):                             #metoda
        return self.name + " wiggle wiggle"


figa = Dog("Figa", "brown", "kundelek", 2)
print(figa.name, figa.color, figa.breed, figa.age)

dyzio = Dog("Dyzio", "dark brown", "jamnik", 4)
print(dyzio.name, dyzio.color, dyzio.breed, dyzio.age)

azor = Dog("Azor", "yellow", "labrador", 5)
print(azor.name, azor.color, azor.breed, azor.age)

print(figa.bark())
print(dyzio.tail_wiggle())