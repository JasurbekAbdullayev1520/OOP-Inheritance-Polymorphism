class User:
    def __init__(self, a):
        self.a = a


    def access_level(self):
        return "Salom"

class Admin(User):
    pass

class Guest(User):
    pass

p = Admin("Ali")
p1 = Guest("Vali")

print(p.access_level(), p.a)
print(p1.access_level(), p1.a)

