# 5▹ Utwórz klasę sklep. Sklep posiada różne produkty. W sklepie można pordukt zobaczyc, przymierzyc, kupic, zwrocic.

class Shop():

    product_list = ["ogrodniczki", "kurtka", "T-Shirt"]
    buy_list = []

    def see_product(self, index):
        print("Oglądam produkt: " + self.product_list[index])

    def try_product(self, index):
        print("Przymierzam produkt: " + self.product_list[index])

    def buy(self, index):
        product_to_buy = self.product_list[index]
        self.buy_list.append(product_to_buy)
        print(f"Kupiłeś: {product_to_buy}")

    def return_product(self, index):
        self.buy_list.pop(index)
        print(f"Zwróciłeś produkt!")


if __name__ == "__main__":
    shop1 = Shop()
    shop1.see_product(1)
    shop1.try_product(2)
    shop1.buy(1)
    shop1.return_product(0)

