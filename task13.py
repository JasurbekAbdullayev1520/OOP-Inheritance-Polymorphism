class Courier:
    def __init__(self, name, product, distens, price):
        self.name = name
        self.product = product
        self.distens = distens
        self.price = price 

    def delivery_range(self):
        return f"{self.name} {self.product}ni {self.distens}km ga yetkazdi"

    def calculate_fee(self):
        return  f"{self.name} tomonidan yetgazilgan mahsulot {self.price}$ "

class BikeCourier(Courier):
    pass
class CarCourier(Courier):
    pass

class DroneCourier(Courier):
    pass

r = BikeCourier("Ali", "pizza", 10, 2)
r1 = CarCourier("Vali", "Fanta", 23, 4)
r3 = DroneCourier("Gani", "Telefon", 21, 2)

print(r.delivery_range(), r.calculate_fee())
print(r1.delivery_range(), r1.calculate_fee())
print(r3.delivery_range(), r3.calculate_fee())
