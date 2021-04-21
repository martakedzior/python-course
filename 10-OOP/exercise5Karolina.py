class Shop:

    def __init__(self, type, size, colour):
        self.type = type
        self.size = size
        self.colour = colour

    def show(self):
        print("Choosen item is:", self.type, "in size",  self.size, "colour:", self.colour)

    def try_on(self, your_size):
        if self.size == your_size:
            print("We got it in your size.")
        else:
            print("This size is out of stock.")

    def buy(self, want_it):
        if want_it == "yes":
            print("Pay please.")
        if want_it == "no":
            print("Maybe next time.")


if __name__ == "__main__":
    cloth = Shop("dress", 38, "blue")
    print(cloth.show())
    cloth.try_on(38)
    cloth.buy("yes")