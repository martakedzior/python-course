import random

class Player:
    """ Gracz w grze strzelance. """

    def blast(self, enemy):
        print('Gracz razi wroga.\n')
        occuracy = random.randint(1, 10)
        if occuracy >= 5:
            enemy.die()
        else:
            enemy.win()



class Alien:

    """ Obcy w grze strzelance. """

    def die(self):
        print('Obcy z trudem łapie oddech, "To już koniec. Ale prawdziwie wielki koniec... \n',
              'Walczyliśmy do końca. Nie, to nie koniec. Larwy moje jednoczcie się! \n',
              'O tak one pomszczą mnie pewnego dnia... \n',
              'Żegnaj, okrutny Wszechświecie! Umieeeraaam"')

    def win(self):
        print("Za słabo..... Obcy zjada Cię!!!\n",
              "Mlask, mlask. Idę spać.... Zieeew!")


if __name__ == '__main__':
    print('************ Śmierć Obcego ************\n')
    hero = Player()
    invader = Alien()
    hero.blast(invader)
    input('\n\nAby zakończyć program, naciśnij klawisz Enter.')
