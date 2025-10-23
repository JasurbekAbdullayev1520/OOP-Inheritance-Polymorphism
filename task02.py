class Vehicle:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def show_info(self):
        return f"{self.name} {self.speed}km/s tezlikda ketayapti"

class Car(Vehicle):
    pass

class Bike(Vehicle):
    pass

s = Car("Cobalt", 123)
s1 = Bike("Veloseped", 12)

print(s.show_info())
print(s1.show_info())