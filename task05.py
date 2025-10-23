class Appliance:
    def __init__(self, name):
        self.name = name

    def turn_on(self):
        return f"{self.name} muaffaqiyatli yoqildi"
    
    def turn_off(self):
        return f"{self.name} muaffaqiyatli o'chirildi"
    
class TV(Appliance):
    pass

class Fridge(Appliance):
    pass

r = TV("Artel TV")
r1 = Fridge("Artel Muzlatgich")

print(r.turn_on())
print(r1.turn_on())

print(r.turn_off())
print(r1.turn_off())