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
class FoodOrder:
    coustomer_name="Aman"
    food_item="Burger"
    quantity=3
    price_per_item=120
    def calculate(self):
        print("Coustomer Name : ",self.coustomer_name)
        print("Food Item : ",self.food_item)
        print("TOtal Bill : ",self.quantity*self.price_per_item)
a=FoodOrder()
a.calculate()




