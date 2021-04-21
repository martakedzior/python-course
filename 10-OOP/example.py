class Dog:
    def __init__(self, name, breed, age):      #konstruktor
        self.name = name
        self.breed = breed
        self.age = age

    def bark(self):                             #metoda
        return "hau " * self.age


# self - metoda bark moze sie wykonac sama na sobie?

figa = Dog("Figa", "kundelek", 2)
print(figa.name, figa.breed, figa.age)

dyzio = Dog("Dyzio", "jamnik", 4)
# print(dyzio.name, figa.breed, figa.age)
# print(figa.bark)


print(Dog.bark(figa))

name = 'reksio'
print(name.capitalize())
print(type(name))

print(dyzio.bark())