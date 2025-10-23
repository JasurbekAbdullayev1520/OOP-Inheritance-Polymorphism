class Animal:
    def __init__(self, a):
        self.a = a
        
    
    def speak(self):
        return "run"

class Dog(Animal):
    pass

class Cat(Animal):
    pass

p = Dog("Spek")
p1 = Cat("Jump")

print(p.speak())
print(p1.speak())




    
    

  

    