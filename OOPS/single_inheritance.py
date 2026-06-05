# Single Inheritance 
# Practice Questions


# Q.1 Library Member System
class Member:
    def __init__(self,name,membership_id):
        self.name=name
        self.membership_id=membership_id

class StudentMember(Member):
    def __init__(self,name,membership_id,course):
        super().__init__(name,membership_id)
        self.course=course

    def display(self):
        print("Member Name :",self.name)
        print("Membership ID :",self.membership_id)
        print("Course Name :",self.course)

s1=StudentMember("Ashu","M101","Python")
s1.display()



# Q.2 Vehicle Registration
class Vehicle:
    def __init__(self,company,model,):
        self.company=company
        self.model=model
        
class Car(Vehicle):
    def __init__(self, company, model, registration_no):
        super().__init__(company, model)
        self.registration_no=registration_no

    def display(self):
        print("Company :",self.company)
        print("Model :",self.model)
        print("Registration :",self.registration_no)

        
c1=Car("Tata","Nexon","MH20AB1234")
c1.display()



# Q.3 Employee Payroll

class Employee:
    def __init__(self, name, salary):
        self.name=name
        self.salary=salary


class Payroll(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus=bonus
    
    def display(self):
        total_salary=self.bonus+self.salary
        print("Employee Name",self.name)
        print("Salary :",self.salary)
        print("Bonus :",self.bonus)
        print("TOtal Salary :",total_salary)

e1=Payroll("Rahul",45000,5000)
e1.display()



# Q.4 Online Course


class Student:
    def __init__(self,name,course):
        self.name=name
        self.course=course

class Enrollment(Student):
    def __init__(self, student, course, duration):
        super().__init__(student, course)
        self.duration=duration

    def display(self):
        print("Student Name :",self.name)
        print("Course :",self.course)
        print("Duration :",self.duration)
        
s1=Enrollment("Priya","Flutter","6 Months")
s1.display()


