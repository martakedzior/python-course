# dziedzicenie wielokrotne
class Ojciec:
    def __init__(self):
        print("Im father!")

    def oblicz_podatki(self):
        print('obliczone podatki')

class Matka:
    def __init__(self):
        print("Im your mother")

    def ucz_programowania(self):
        print('Ucz się Pythona!')

class Dziecko(Ojciec, Matka):
    pass


baby = Dziecko()
baby.oblicz_podatki()
baby.ucz_programowania()