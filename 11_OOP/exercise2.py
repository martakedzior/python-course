#2▹ Do klasy człowiek dodaj metodę super() tak, aby móc wyświetlić opis dostępny gdziekolwiek w klasie ssaki.

class Zwierzeta():
    def __init__(self):
        print("Im an Animal!")

    def eat(self):
        print("Zeby zyc muszę jeść!")


class Ssaki(Zwierzeta):
    def __init__(self):
        print("Jak jestem mały to ssam mleko matki!")

class Kot(Ssaki):
    print("Jestem kotkiem")

class Pies(Ssaki):
    print("Jestem pieskiem")

class Czlowiek(Ssaki):
    def __init__(self):
        print("Jestem czlowiekiem")
        super().__init__()



if __name__ == "__main__":
    kot = Kot()
    kot.eat()

    pies = Pies()
    pies.eat()

    marta = Czlowiek()
    marta.eat()
