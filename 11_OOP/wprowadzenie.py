class Canis:
    paws = 4

    def __init__(self):
        print("Canis is a genus, family: Canidae")

    def show_description(self):
        print('''Species of this genus are distinguished
           by their moderate to large size, their massive,
           well-developed skulls and dentition,
           long legs, and comparatively short ears and tails''')


class Dog(Canis):
    kingodom = 'Animals' #atrybut klasy, zmienna wspólna dla wszystkich obiektów klasy Pies

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def show_description(self):
        super(Dog, self).show_description()
        print('''Dog s a member of the genus Canis (canines),
            which forms part of the wolf-like canids.''')

    def bark(self, sound='uf'):  #domyślna wartość parametru
        print(sound * self.age)

if __name__ == "__main__":
    dyzio = Dog('Dyzio', 3, 'mops')
    dyzio.bark()
    dyzio.bark('hauu')
    print(dyzio.paws)
    dyzio.show_description()
