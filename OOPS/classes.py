class Student:

    name="class name"
    course="class course"

    def __init__(self,name,course):
        self.name=name
        self.course=course
    
    def display(self):
        print("Student Name :",self.name)
        print("Student Course :",self.course)

std1=Student("Ritesh","MCA")
std2=Student("Ashutosh","Flutter")
std1.display()
std2.display()




class Employee:

    company="Tech Solution"
    count=0

    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        Employee.count+=1
        
    def display(self):
        print("Employee Name :",self.name)
        print("Employee Salary :",self.salary)
        print("Company Name :",self.company)
        print("---------------------------------")

    @classmethod
    def show(self):
        print("Total Employee:",self.count)

e1=Employee("Ritesh",50000)
e2=Employee("Aman",45000)
e3=Employee("Neha",60000)
e1.display()
e2.display()
e3.display()
Employee.show()



class BankAccount:

    def __init__(self,name,balance):
        self.name=name
        self.balance=balance

    def deposit(self,amount):
        self.balance+=amount

    def withdraw(self,amount):
        if self.balance>amount:
            self.balance=self.balance-amount
        else:
            print("Insufficient Balance")

    
    def display(self):
        print("Account Holder Name :",self.name)
        print("Current Balance :",self.balance)


a1=BankAccount("Ritesh",5000)
a2=BankAccount("Aman",3000)
a1.deposit(2000)
a2.withdraw(1000)
a1.display()
a2.display()