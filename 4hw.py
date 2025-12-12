class Product:
    def _init_(self, title, price, quantity):
        self.title = title
        self.price = price
        self.quantity = quantity

    def _str_(self):
        return self.title + " = " + str(self.price) + "р (" + str(self.quantity) + ")"

    def _repr_(self):
        return "Product(" + self.title + ", " + str(self.price) + ", " + str(self.quantity) + ")"

    def _eq_(self, other):
        if self.title == other.title:
            return True
        else:
            return False

    def _lt_(self, other):
        return self.price < other.price

    def _add_(self, other):
        combo_price = self.price + other.price
        return Product("Combo", combo_price, 1)