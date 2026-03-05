class Employee:
    
    def __init__(self, name, salary, designation):
        self.name = name
        self.salary = salary
        self.designation = designation

    def display(self):
        print(f"Employee Name : {self.name}")
        print(f"Designation   : {self.designation}")
        print(f"Salary        : {self.salary}")
 

class Manager(Employee):
    def __init__(self, name, salary, designation):
        super().__init__(name, salary, designation)
    def calculate_bonus(self, bonus_percent):
        self.salary += self.salary * (bonus_percent / 100)
        return self.salary

tuhin=Manager("Tuhin",15000,"Manager")
tuhin.display()
print(f"After bonus the salary is :{ tuhin.calculate_bonus(15)}")