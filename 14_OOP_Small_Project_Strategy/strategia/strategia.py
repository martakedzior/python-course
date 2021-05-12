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

    rycerze = []

    for i in range(4):
        rycerze.append(Rycerz())

    print(rycerze)

    for rycerz in rycerze:
        rycerz.maszeruj(2000)

    rycerze.append(Rycerz())

    for rycerz in rycerze:
        rycerz.atakuj()

    print("Oddział! Baczność!")
    for rycerz in rycerze:
        print(rycerz)


    lucznicy = []

    for l in range(3):
        lucznicy.append(Lucznik())

    armia = rycerze + lucznicy

    print("Armia")
    for wojownik in armia:
        print(wojownik)

    for wojownik in armia:
        wojownik.atakuj()

    print("Armia po ataku")
    for wojownik in armia:
        print(wojownik)


if __name__ == "__main__":
    main()
