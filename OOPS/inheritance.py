class Employee:
    
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        
class Manager(Employee):
    def __init__(self, name, salary,department):
        super().__init__(name, salary)
        self.department=department


    def display(self):
        print("Employee Name :",self.name)
        print("Employee salary :",self.salary)
        print("Employee Department :",self.department)



manager=Manager("Ritesh",30000,"Sales")
manager.display()
