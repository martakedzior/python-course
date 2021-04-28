# 1▹ Korzystając z wikipedii utwórz klasy - Kot, Pies, Człowiek. Każda z nich powinna dziedziczyć z nadrzędnej klasy Ssaki.
# Klasa Ssaki powinna dziedziczyć z klasy Zwierzęta.
# Utwórz obiekty klas - kot, pies i człowiek, udowodnij, że rzeczywiście korzystają z klas rodziców.


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
    print("Jestem czlowiekiem")


if __name__ == "__main__":
    kot = Kot()
    kot.eat()

    pies = Pies()
    pies.eat()

    marta = Czlowiek()
    marta.eat()
