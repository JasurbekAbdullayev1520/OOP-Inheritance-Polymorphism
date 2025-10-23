class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_bonus(self):
        return f"{self.name} {self.salary * 0.1}$ bons oladi"
    
class Developer(Employee):
    pass

class Manager(Employee):
    def calculate_bonus(self):
        return f"{self.name} {self.salary * 0.2}$ bons oladi"
    
r = Developer("Vali", 20000)
r1 = Manager("Ali", 2500000)

print(r.calculate_bonus())
print(r1.calculate_bonus())