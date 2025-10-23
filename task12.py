class User:
    def __init__(self, name, course):
        self.name = name
        self.course = course

    def get_dashboard(self):
        return f"{self.name}  {self.course} ga boradi"

class Student(User):
    pass

class Instructor(User):
    def __init__(self, course, price):
       self.course = course
       self.price = price 
    def get_dashboard(self):
        return f"{self.course} kursi {self.price}so'm"
    
r = Student("Ali", "Matematika")
r1 = Instructor("Matematika", 50000)

print(r.get_dashboard())
print(r1.get_dashboard())