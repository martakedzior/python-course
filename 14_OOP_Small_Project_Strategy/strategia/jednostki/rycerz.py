from wojownik import Wojownik

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
