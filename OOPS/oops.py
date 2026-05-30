# Check wheather a person can vote or not 
# class citizen:
#     def checkvoting(self,name,age):
#         print("Name : ",name)
#         print("Eligible for voting" if age>=18 else "Not eligible for Voting")

# abc=citizen()
# abc.checkvoting("Ritesh",16)




# Student information display
# class student:
#     student_name="Rahul"
#     student_age=19
#     def details(self):
#         print(f"Student Name : {self.student_name}")
#         print(f"Student Age : {self.student_age}")
# a=student()
# a.details()



# ATM balance checker 
# class atm:
#     account_holder="Aman"
#     balance=4500
#     def details(self):
#         print("Account Holder :",self.account_holder)
#         print("Available Balance :",self.balance)
# a=atm()
# a.details()



# Employee salary increment 
# class employee:
#     salary=25000
#     increment=3000
#     def calculate(self):
#         print("Old salary :",self.salary)
#         self.salary=self.salary+self.increment
#         print("Updated salary :",self.salary)
# a=employee()
# a.calculate()



# Even Odd Checker
# class number:
#     num=31
#     def evenorodd(self):
#         print(f"{self.num} is Even" if self.num%2==0 else f"{self.num} is Odd")
# a=number()
# a.evenorodd()














































# class student:
#     name="Ashu"
#     course="Python"
#     def display(self,name,course):
#         print(f"Student Name : {self.name}")
#         print(f"Student Course : {self.course}")
# # a=student()
# # a.display("Ritesh","Java")
#     def __init__(self,name,course):
#         self.name=name
#         self.course=course
#         print(self.name)
#         print(name)
# s1=student("Ritesh","Java")
# print(s1.name)


# class person:
#     name="Ritesh"
#     learning="Programming"
#     def info(self):
#         print(f"{self.name} is learning {self.learning}")    

# a=person()
# a.name="Gaurav"
# a.learning="Cricket"
# a.info()





# A food delivery app wants to calculate the final bill amount of an order
# class FoodOrder:
#     coustomer_name="Aman"
#     food_item="Burger"
#     quantity=3
#     price_per_item=120
#     def calculate(self):
#         print("Coustomer Name : ",self.coustomer_name)
#         print("Food Item : ",self.food_item)
#         print("TOtal Bill : ",self.quantity*self.price_per_item)
# a=FoodOrder()
# a.calculate()



# Student attendance tracker 
# class attendance:
#     student_name="Aman"
#     total_classes=50
#     attend_classes=42
#     percentage=(attend_classes/total_classes)*100
#     def calculate(self,student_name):
#         print("Student Name :",student_name)
#         print("Attendance Percentage :",self.percentage)
#         print("Eligible for exam" if self.percentage>75 else "Not Eligible")

# a=attendance()
# a.calculate("Ritesh")





class student:
    name="Gaurav"
    course="Java"

    def display(self,name,course):
        print("Name -->>",name)
        print("Course -->>",course)

s1=student()
s2=student()
s1.display("Ritesh","Python")
s2.display("Ashutosh","Flutter")














# class Employee:

#     companyName = "Techno Amaze"

#     def displayData(self): # instance method
#         self.username = "Ashutosh"
#         print("Within display data")
#         print(f"Instance variable : {self.username}")
#         print(f"Instance variable : {Employee.username}")

#     @classmethod # decorator
#     def classMethod(self): # class method
#         print("Class method , ", self.companyName)
#         print("Class method , ", Employee.companyName)

#     def instanceMethod(self):
#         print("Class method , ", self.username)
#         print("Class method , ", self.companyName)
#         print("Class method , ", Employee.username)
#         print("Class method , ", Employee.companyName)

#     @staticmethod
#     def staticMethod(value):
#         print("Within static method. - username ", value)
#         print("Within static method. - companyname", Employee.companyName)


# e1 = Employee()

# # e1.displayData()
# print("Class Variable : ", e1.companyName)
# e1.classMethod()
# # e1.instanceMethod()
# e1.staticMethod(77)

# print(e1)
# print(e1.instanceMethod)
# print(e1.classMethod)
# print(e1.staticMethod)