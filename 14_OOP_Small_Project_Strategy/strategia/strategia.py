from jednostki.rycerz import Rycerz
from jednostki.lucznik import Lucznik


def main():
    zagloba = Rycerz()
    zagloba.maszeruj(5)
    zagloba.atakuj()
    print(zagloba)

    potahontas = Lucznik()
    potahontas.maszeruj(8)
    potahontas.atakuj()
    print(potahontas)
    potahontas.atakuj()
    potahontas.atakuj()
    potahontas.atakuj()
    potahontas.atakuj()
    potahontas.atakuj()


if __name__ == "__main__":
    main()
