class Wojownik:
    def __init__(self):
        self._doswiadczenie = 0

    def __repr__(self):
        nazwa = self.__class__.__name__
        return f"{nazwa}: hp={self._zycie}, exp={self._doswiadczenie}"

    def maszeruj(self, dystans):
        nazwa = self.__class__.__name__
        print(f"{nazwa}: Przeszedłem {dystans} m")
        self._doswiadczenie += 0.02 * dystans


class Rycerz(Wojownik):
    def __init__(self):
        super().__init__()
        self._zycie = 60

    def maszeruj(self, dystans):
        print("Rycerz: Przeszedłem {} m".format(dystans))
        self._doswiadczenie += dystans * 0.2

    def atakuj(self):
        print("Rycerz: Machnąłem mieczem!")
        self._doswiadczenie += 0.3


class Lucznik(Wojownik):
    def __init__(self):
        super().__init__()
        self._zycie = 40
        self.liczba_strzal = 5

    def maszeruj(self, dystans):
        print("Lucznik: Przeszedłem {} m".format(dystans))
        self._doswiadczenie = self._doswiadczenie + dystans * 0.2

    def atakuj(self):
        if self.liczba_strzal == 0:
            print("Lucznik: Nie mam juz strzał!")
        else:
            print("Lucznik: Wypuściłem strzałę!")

        self._doswiadczenie += 0.4
        self.liczba_strzal -= 1



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
