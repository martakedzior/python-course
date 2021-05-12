from wojownik import Wojownik

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


