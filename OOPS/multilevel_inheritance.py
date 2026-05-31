# Q.1 College Management 

class College:
    def __init__(self,college):
        self.college=college

class Department(College):
    def __init__(self, college,department):
        super().__init__(college)
        self.department=department

class Student(Department):
    def __init__(self, college, department, student):
        super().__init__(college, department)
        self.student=student

    def display(self):
        print("College :",self.college)
        print("Department :",self.department)
        print("Student :",self.student)

s1=Student("Techno Amaze College","Computer Science","Rohan")
s1.display()




# Q.6 Banking System 

class Bank:
    def __init__(self, bank):
        self.bank=bank

class Branch(Bank):
    def __init__(self, bank, branch):
        super().__init__(bank)
        self.branch=branch

class Account(Branch):
    def __init__(self, bank, branch, account):
        super().__init__(bank, branch)
        self.account=account

    def display(self):
        print("Bank :",self.bank)
        print("Branch :",self.branch)
        print("Account Holder :",self.account)

a1=Account("SBI","Aurangabad","Amit")
a1.display




# Q.7 Product Delivery

class Product:
    def __init__(self, product):
        self.product=product

class Warehouse(Product):
    def __init__(self, product, warehouse):
        super().__init__(product)
        self.warehouse=warehouse
    
class Delivery(Warehouse):
    def __init__(self, product, warehouse, coustomer):
        super().__init__(product, warehouse)
        self.coustomer=coustomer

    def display(self):
        print("Product :",self.product)
        print("Warehouse :",self.warehouse)
        print("Coustomer :",self.coustomer)

c1=Delivery("Laptopl","Pune","Ashutosh")
c1.display()




# Q.8 Hospital Management

class Hospital:
    def __init__(self, hospital):
        self.hospital=hospital

class Doctor(Hospital):
    def __init__(self, hospital, doctor):
        super().__init__(hospital)
        self.doctor=doctor

class Patient(Doctor):
    def __init__(self, hospital, doctor, patient):
        super().__init__(hospital, doctor)
        self.patient=patient

    def display(self):
        print("Hospital :",self.hospital)
        print("Doctor :",self.doctor)
        print("Patient :",self.patient)

p1=Patient("City Care","Dr.Sharma","Neha")
p1.display()