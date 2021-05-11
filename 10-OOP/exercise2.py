# 2▹ Utwórz klasę dla storczyków. Storczyki z zasady mają różne kolory, pory kwitnienia, gatunki.
# Utwórz dowolne atrybuty i metody. Dodaj atrybut wspólny dla wszystkich storczyków - królestwo roślin.
# Utwórz kilka storczyków z różnymi parametrami.

class Orchid():
    def __init__(self, kingdom, colour, season, breed):
        self.kingdom = kingdom
        self.colour = colour
        self.season = season
        self.breed = breed

    def blossom(self):
        return self.breed + " blossoms"


orchid1 = Orchid("Kingdom of plants", "yellow", "winter", "orchid1")

print(orchid1.colour, orchid1.season, orchid1.breed)

orchid1 = Orchid("Kingdom of plants", "yellow", "winter", "orchid1")
orchid2 = Orchid("Kingdom of plants", "fuchsia", "spring", "orchid2")
orchid3 = Orchid("Kingdom of plants", "white", "summer", "orchid3")

print(orchid3.blossom())
