# inheritance
class Animals():
    def __init__(self):
        print("Im an Animal")

    def eat(self):
        print("Am am am")


class Warm_blooded(Animals):
    def wyleguj_sie(self):
        print("Leżę na słoneczku!")


class Dog(Warm_blooded):
    def __init__(self):
        print("Im a Dog")

    def eat(self):
        print("I am a Dog and I eat fast")

    def wyleguj_sie(self):
        super().wyleguj_sie()
        print("Im a Dog and I am lying on couch")


dyzio = Dog()
dyzio.eat()
dyzio.wyleguj_sie()

kot = Warm_blooded()
kot.eat()
kot.wyleguj_sie()