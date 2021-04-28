# 3▹ Zadanie inspirowane popkulturą: https://www.youtube.com/watch?v=Ct6BUPvE2sM
#
# Stwórz klasę PenPinapple, która dziedziczy z klas Pen oraz Pinapple. Logiki to nie ma, więc dodaj wg uznania.

class Pen:
    def __init__(self):
        print('Pen!')


class Pinapple():
    def scream(self):
        print('Pinapple')


class PenPinapple(Pen, Pinapple):
    def __init__(self):
        print('~~~~')
        super().__init__()
        super().scream()


if __name__ == "__main__":
    pppp = PenPinapple()