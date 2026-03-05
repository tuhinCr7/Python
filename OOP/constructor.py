class Employee:
    
    def __init__(self,name,salary,designation):
        print("Thanks for creating an object")
        self.name=name
        self.salary=salary
        self.designation=designation
    def display(self):
        print(f" Employee Name : {self.name} Designation : {self.designation} salary : {self.salary}") 

tuhin=Employee("Tuhin",15000,"Manager")
tuhin.display()