class Rycerz:
    def __init__(self):
        self.zycie = 60
        self.doswiadczenie = 0

    def __repr__(self):
        return print("Rycerz: hp={}, exp={}".format(self.zycie, self.doswiadczenie))

    def maszeruj(self, dystans):
        self.doswiadczenie = self.doswiadczenie + dystans * 0.2
        return print("Rycerz: Przeszedłem {} m".format(dystans))

    def atakuj(self):
        self.doswiadczenie = self.doswiadczenie + 0.3
        return print("Rycerz: Machnąłem mieczem!")



if __name__ == "__main__":
    zagloba = Rycerz()
    zagloba.maszeruj(5)
    zagloba.atakuj()
    zagloba.__repr__()
