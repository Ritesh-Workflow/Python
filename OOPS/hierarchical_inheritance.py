# Q.9 Employee Roles

# class Employee:
#     def __init__(self,name):
#         self.name=name


# class Manager(Employee):
#     def __init__(self, name,department):
#         super().__init__(name)
#         self.department=department

#     def display(self):
#         print("Employee Name :",self.name)
#         print("Department :",self.department)
    
# class Staff(Employee):
#     def __init__(self, name,designation):
#         super().__init__(name)
#         self.designation=designation

#     def display(self):
#         print("Employee Name :",self.name)
#         print("Designation :",self.designation)
# print("------------Q.9 Answer:-------------")
# obj1=Manager("Sandeep","Sales")
# obj2=Staff("Sandeep","Clerk")
# obj1.display()
# obj2.display()



# print("------------Q.10 Answer:-------------")
# Q.10 Educational Institute 

# class Institute:
#     def __init__(self,institute):
#         self.institute=institute

# class Teacher(Institute):
#     def __init__(self, institute, teacher):
#         super().__init__(institute)
#         self.teacher=teacher

#     def display(self):
#         print("Institute :",self.institute)
#         print("Teacher :",self.teacher)

# class Student(Institute):
#     def __init__(self, institute, student):
#         super().__init__(institute)
#         self.student=student

#     def display(self):
#         print("Institute :",self.institute)
#         print("Student :",self.student)

# T1=Teacher("Techno Amaze Academy","Rushi Sir")
# S1=Student("Techno Amaze Academy","Ashu")
# T1.display()
# S1.display()



# print("------------Q.11 Answer:-------------")
# Q.11 Animal Information 

# class Animal:
#     def __init__(self,animal):
#         self.animal=animal

# class Dog(Animal):
#     def __init__(self, animal, dog):
#         super().__init__(animal)
#         self.dog=dog

#     def display(self):
#         print("Animal Type :",self.animal)
#         print("Dog Name",self.dog)

# class Cat(Animal):
#     def __init__(self, animal,cat):
#         super().__init__(animal)
#         self.cat=cat

#     def display(self):
#         print("Animal Type :",self.animal)
#         print("Cat Name :",self.cat)

# D1=Dog("Mammal","Bruno")
# C1=Cat("Mammal","Kitty")
# D1.display()
# C1.display()



# print("------------Q.12 Answer:-------------")
# Q.12 Store Inventory 

# class Store:
#     def __init__(self, store):
#         self.store=store

# class Grocery(Store):
#     def __init__(self, store, grocery_item):
#         super().__init__(store)
#         self.grocery_item=grocery_item

#     def display(self):
#         print("Store :",self.store)
#         print("Grocery item :",self.grocery_item)

# class Electonic(Store):
#     def __init__(self, store, electronic_item):
#         super().__init__(store)
#         self.elctronic_item=electronic_item
    
#     def display(self):
#         print("Store :",self.store)
#         print("Electronic item :",self.elctronic_item)

# G1=Grocery("Mega Mart","Rice")
# E1=Electonic("Mega Mart","Televison")
# G1.display()
# E1.display()




print("-------------------------Q.1 ANSWER :----------------------------")
# Q.1 Salary management system

class Employee:
    def __init__(self,salary=25000):
        self.salary=salary

    def calculateSalary(self):
        print("Employee Salary :",self.salary)


class Manager(Employee):
    def __init__(self, salary=50000,allowance=10000):
        super().__init__(salary)
        self.allowance=allowance
        self.total_salary=salary+allowance

    def calculateSalary(self):
        print("Manager Salary :",self.total_salary)


class Developer(Employee):
    def __init__(self, salary=40000,bonus=5000):
        super().__init__(salary)
        self.bonus=bonus
        self.total_salary=salary+bonus

    def calculateSalary(self):
        print("Developer Salary :",self.total_salary)

    
class Intern(Employee):
    def __init__(self, salary=12000):
        super().__init__(salary)
       
    def calculateSalary(self):
        print("Intern Stipend :",self.salary)


employee=Employee()
manager=Manager()
developer=Developer()
intern=Intern()
employee.calculateSalary()
manager.calculateSalary()
developer.calculateSalary()
intern.calculateSalary()



print("-------------------------Q.2 ANSWER :----------------------------")
# Q.2 Notification Management System

class Emailnotification:
    def sendNotification(self):
        print("Email sent succesfully")

class SMSNotification:
    def sendNotification(self):
        print("SMS sent succesfully")

class WhatsappNotification:
    def sendNotification(self):
        print("SMS sent succesfully")

email=Emailnotification()
sms=SMSNotification()
whatsapp=WhatsappNotification()
email.sendNotification()
sms.sendNotification()
whatsapp.sendNotification()



print("-------------------------Q.3 ANSWER :----------------------------")
# Q.3 Online Payment System

class UPIPayment:
    def makePayment(self):
        print("Payment completed using UPI")

class CreditCardPayment:
    def makePayment(self):
        print("Payment completed using Credit Card")

class NetBanking:
    def makePayment(self):
        print("Payement completed by Net Banking")

upi=UPIPayment()
creditCard=CreditCardPayment()
netBanking=NetBanking()
upi.makePayment()
creditCard.makePayment()
netBanking.makePayment()



print("-------------------------Q.4 ANSWER :----------------------------")
# Q.4 Vehicle speed information system

class Vehicle:
    def __init__(self,speed):
        self.speed=speed

class Bike(Vehicle):
    def __init__(self, speed):
        super().__init__(speed)

    def showSpeed(self):
        print(f"Bike Speed :{self.speed} km/hr")

class Car(Vehicle):
    def __init__(self, speed):
        super().__init__(speed)

    def showSpeed(self):
        print(f"Car Speed :{self.speed} km/hr")

class Train(Vehicle):
    def __init__(self, speed):
        super().__init__(speed)

    def showSpeed(self):
        print(f"Train Speed :{self.speed} km/hr")

bike=Bike(80)
car=Car(120)
train=Train(180)
bike.showSpeed()
car.showSpeed()
train.showSpeed()



print("-------------------------Q.5 ANSWER :----------------------------")
# Q.5 Library dashboard system

class Student:
    def accesDashboard(self):
        print("Student Dashboard Opened")

class Coordinator:
    def accesDashboard(self):
        print("Coordinator Dashboard Opened")

class Admin:
    def accesDashboard(self):
        print("Admin Dashboard Opened")

student=Student()
coordinator=Coordinator()
admin=Admin()
student.accesDashboard()
coordinator.accesDashboard()
admin.accesDashboard()


print("-------------------------Q.6 ANSWER :----------------------------")
# Q.6 Banking Interest System

class Account:
    def __init__(self,interest):
        self.interest=interest

class SavingAccount(Account):
    def __init__(self,interest,amount):
        super().__init__(interest)
        self.amount=amount
        interest=(amount/100)*interest
        self.total_amt=amount+interest

    def calculateInterest(self):
        print(f"Saving Account Balance With Interest :{self.total_amt}")

class CurrentAccount(Account):
    def __init__(self, interest, amount):
        super().__init__(interest)
        self.amount=amount
        interest=(amount/100)*interest
        self.total_amt=amount+interest

    def calculateInterest(self):
        print(f"Current Account Balance With Interest :{self.total_amt}")

class FixedDeposit(Account):
    def __init__(self, interest, amount):
        super().__init__(interest)
        self.amount=amount
        interest=(amount/100)*interest
        self.total_amt=amount+interest

    def calculateInterest(self):
        print(f"Fixed Deposit Balance With Interest :{self.total_amt}")


savingAccount=SavingAccount(10,30000)
currentAccount=CurrentAccount(6,30000)
fixedDeposit=FixedDeposit(7,30000)

savingAccount.calculateInterest()
currentAccount.calculateInterest()
fixedDeposit.calculateInterest()




