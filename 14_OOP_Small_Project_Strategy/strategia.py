class Rycerz:
    def __init__(self):
        self._zycie = 60
        self._doswiadczenie = 0

    def __repr__(self):
        return f"Rycerz: hp={self._zycie}, exp={self._doswiadczenie}"

    def maszeruj(self, dystans):
        print("Rycerz: Przeszedłem {} m".format(dystans))
        self._doswiadczenie = self._doswiadczenie + dystans * 0.2

    def atakuj(self):
        print("Rycerz: Machnąłem mieczem!")
        self._doswiadczenie += 0.3


def main():
    zagloba = Rycerz()
    zagloba.maszeruj(5)
    zagloba.atakuj()
    print(zagloba)


if __name__ == "__main__":
    main()
