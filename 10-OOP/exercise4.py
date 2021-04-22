# 4▹ Pomyśl co sprawia, że ssak jest ssakiem? Utwórz klasę ssaki. Stwórz kilka obiektów klasy ssaki np. wilk, koń, ssaki.


class Mammals():
    def __init__(self, name, covered_with, breathe_with, blood_system):
        self.name = name
        self.covered_with = covered_with
        self.breathe_with = breathe_with
        self.blood_system = blood_system

    def feed_young(self):
        return self.name + " feeds young mammal with milk."


dog = Mammals("German sheppard", "fur", "lungs", "warm-blooded")

print(dog.name, dog.covered_with, dog.breathe_with, dog.blood_system)

elephant = Mammals("African savannah elephant,", "skin with hear", "lungs", "warm-blooded")
wolf = Mammals("Gray wolf", "fur", "lungs", "warm-blooded")

print(dog.feed_young())
print(elephant.feed_young())