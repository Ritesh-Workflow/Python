# class Employee:
    
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
        
# class Manager(Employee):
#     def __init__(self, name, salary,department):
#         super().__init__(name, salary)
#         self.department=department


#     def display(self):
#         print("Employee Name :",self.name)
#         print("Employee salary :",self.salary)
#         print("Employee Department :",self.department)



# manager=Manager("Ritesh",30000,"Sales")
# manager.display()




# class Vehicle:

#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model

    
# class Car(Vehicle):
    
#     def __init__(self, brand, model,fuel):
#         print("Z")
#         super().__init__(brand, model)
#         self.fuel=fuel

#     def display(self):
#         print("Brand :",self.brand)
#         print("Model :",self.model)
#         print("Fuel Type :",self.fuel)

# c1=Car("BMW","M5","Disel")
# c1.display()




# class Vehicle: # base , parent

#     company = "BMW"
#     _model = 'M5'
#     __price = 70000000

#     def __init__(self):
#         print("within vehicle constructor")
#         self.name = "Techno Amaze Academy"

#     def displayData(self):
#         print("Within Display Data Method of Vehicle")

# class Car(Vehicle): # child , derived

#     def __init__(self):
#         super().__init__()
#         super().displayData()
#         print("within Car constructor")

#     def data(self):
#         super().__init__()
#         print("Within data of Car")
#         print(self.name)
#         Vehicle.displayData(self)
#         print(self.company)
#         print(Vehicle.company)
#         print(Vehicle._model)
#         print(self._model)


# vehicle = Vehicle()
# car = Car()

# vehicle.displayData()
# car.displayData()
# print("--------------------------------------")
# car.data()



# class Employee:

#     def __init__(self,name,salary):
#         self.name = name
#         self.salary = salary


# class Manager(Employee):

#     def __init__(self, name, salary , department): # constructor for manager
#         super().__init__(name, salary) # calling parent constructor
#         self.department = department

#     def displayData(self):
#         print("Employee name : ", self.name)
#         print("Employee Salary : ", self.salary)
#         print("Employee Department : ", self.department)

#class Staff(Manager):
   
#    def __init__(self, name, salary): # Emploee as a parent
#        super().__init__(name, salary)

    # def __init__(self, name, salary, department): # Manager as a parent
    #     super().__init__(name, salary, department)

    # def __init__(self, name, salary, department):
    #     super().__init__(name, salary, department)

    # def data(self):
    #     super().displayData()
    #     print("Within a data method of staff class.")

# manager = Manager("Sandeep" , 90000 , "Sales")
# manager.displayData()

# staff = Staff("Sandeep" , 90000 , "Sales")
# staff.data()
        


class Employee:

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary


class Manager(Employee):

    def __init__(self, name, salary , department): # constructor for manager
        super().__init__(name, salary) # calling parent constructor
        self.department = department
        self.manager = "Manager"

    def displayData(self):
        print("Employee name : ", self.name)
        print("Employee Salary : ", self.salary)
        print("Employee Department : ", self.department)

class Staff(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department
        self.staff = "staff"

    def displayData(self):
        print("Employee name : ", self.name)
        print("Employee Salary : ", self.salary)
        print("Employee Department : ", self.department)
        print("----->",self.name)


staff = Staff("Ashish Staff" , 10000 , "Shop Keeper")
manager = Manager("Sandeep Manager" , 15000 , "Sales Department")

staff.staff
manager.manager
staff.name
manager.name

staff.displayData()
manager.displayData()