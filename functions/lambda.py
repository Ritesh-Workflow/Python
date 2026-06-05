
x=5
square=lambda x:x*
print(square(9))

# x=5
# a=lambda x: "Even" if (x%2==0) else"Odd"
# print(a)

# evenOdd =lambda x: "Even" if (x%2==0) else"Odd"
# print(evenOdd(5))
# num=21
# print("Even" if(num%2==0) else"Odd")

# value=True
# for i in range(4):
#     print(i)
# else: 
#     value=False
#     print("After for loop")

# bonusMarks=lambda marks: marks+5
# print("Bonus Marks:",bonusMarks(45))


# bill=lambda unit,rate:unit*rate
# print("Total Bill :",bill(120,8))

# salary=lambda salary1,salary2: salary1 if (salary1>salary2) else salary2
# print(salary(12000,1500))

# discount=120
# amount=lambda amt: amt-discount 
# print("Final Amount :",amount(850))

# value = amount(850)

# greaterOrnot=lambda : "Amount is greater than 500" if (value>500) else"Amount is not greater"
# print(greaterOrnot())

# def sum(a,b):
#     return (a+b)
# a=sum(10,20)
# print(a)

# sum=lambda num1,num2:num1+num2
# a=sum(10,20)
# print(a)

#Question 1 — Movie Ticket Price Calculator
# A cinema hall wants to calculate total ticket cost for a group booking.
# Given Data:
# ticket_price = 180
# persons = 4
# Perform the following:
# Create lambda function
# Calculate total ticket amount
# Print total bill
# Expected Output:
# # Total Ticket Cost: 720
# ticketAmount=lambda titckets,ticket_price: ticket_price*titckets
# print("Total Ticket Cost: ",ticketAmount(4,180))



# # Question 2 — Student Grade Checker
# # A school wants to assign grades to students based on marks.
# # Given Data:
# # marks = 76
# # Perform the following:
# # Create lambda function
# # Check grade condition
# # Print grade
# # Expected Output:
# # Grade B
# gradeChecker=lambda marks:"Grade A" if (marks>80) else"Grade B" if(marks>60) else"Grade C" if(marks>35) else"Fail"
# print(gradeChecker(36))



# # Question 3 — Courier Weight Charge System
# # A courier company wants to calculate delivery charges.
# # Given Data:
# # weight = 6
# # charge_per_kg = 45
# # Perform the following:
# # Create lambda function
# # Calculate courier charge
# # Print total charge
# # Expected Output:
# # Courier Charge: 270
# courierCharge=lambda charge_per_kg,weight:charge_per_kg*weight
# charge=courierCharge
# print("Courier Charge: ",charge(45,6))


# # Question 4 — Employee Overtime Payment
# # A company wants to calculate overtime salary.
# # Given Data:
# # hours = 5
# # rate = 300
# # Perform the following:
# # Create lambda function
# # Multiply overtime hours with rate
# # Print overtime payment
# # Expected Output:
# # Overtime Payment: 1500
# overTime_payment=lambda hours,rate:hours*rate
# print("Overtime Payment: ",overTime_payment(5,300))



# # Question 5 — Age Category System
# # A company wants to categorize applicants.
# # Given Data:
# # age = 16
# # Perform the following:
# # Create lambda function
# # Check age condition
# # Print category
# # Expected Output:
# # Minor
# category=lambda age:"Minor" if (age<18) else "Adult"
# print(category(16))



# # Question 6 — Petrol Cost Calculator
# # A traveler wants to calculate petrol expenses.
# # Given Data:
# # liters = 8
# # price_per_liter = 106
# # Perform the following:
# # Create lambda function
# # Calculate petrol cost
# # Print total amount
# # Expected Output:
# # Total Petrol Cost: 848
# petrolCost=lambda liters,price_per_litre:liters*price_per_litre
# print("Total Petrol Cost: ",petrolCost(8,106))



# # Question 7 — Hotel Room Booking Eligibility
# # A hotel wants to verify whether customers can book premium rooms.
# # Given Data:
# # customer_age = 22
# # Perform the following:
# # Create lambda function
# # Check booking eligibility
# # Print result
# # Expected Output:
# # Eligible for Premium Room
# eligibility=lambda age:"Eligible for Premium Room" if (age>18) else "Not Eligible"
# print(eligibility(17))



# # Question 8 — Cricket Strike Rate Calculator
# # A cricket academy wants to calculate strike rate.
# # Given Data:
# # runs = 75
# # balls = 50
# # Perform the following:
# # Create lambda function
# # Calculate strike rate
# # Print strike rate
# # Expected Output:
# # Strike Rate: 150.0
# strikeRate=lambda runs,balls: (runs/balls)*100
# print(strikeRate(75,50))



# # Question 9 — Bank Loan Eligibility
# # A bank wants to check loan eligibility.
# # Given Data:
# # salary = 42000
# # Perform the following:
# # Create lambda function
# # Verify salary condition
# # Print eligibility result
# # Expected Output:
# # Eligible for Loan
# loanELigibility=lambda salary: "Eligible for Loan" if (salary>25000) else "Not Eligible For Loan"
# print(loanELigibility(2000))



# # Question 10 — Mobile Password Strength Checker
# # A mobile app wants to verify whether the password length is strong enough.
# # Given Data:
# # password_length = 10
# # Perform the following:
# # Create lambda function
# # Check password length
# # Print password status
# # Expected Output:
# # Strong Password
# streanthChecker=lambda password: "Strong Password" if(len(password)>10) else "Enter Strong Paasword"
# print(streanthChecker("@Ritesh1234"))




#map() & filter() functions:

#Increase salary by 2000
salary=[18000,22000,25000,30000]
result=map(lambda x: x+2000,salary)
print(list(result))


# #add 18% gst 
prices=[500,800,1250,300]
result2=map(lambda a:a+(a*18)/100,prices)
print(list(result2))


#Generate pass/fail status for student
marks=[78,35,55,29,91]
result3=map(lambda mark:"Pass" if mark>=35 else"Fail",marks)
print(list(result3))


#A company wants to store only even order IDs
order_ids=[101,204,305,408,512,617]
even_no=filter(lambda num: num%2==0,order_ids )
print(list(even_no))


#Diisplay product costing more than 1000
prices=[450,1200,850,2200,999,1500]
result4=filter(lambda price: price>1000,prices)
print(list(result4))

# A Library management system wants to show only available seats
seats=[0,1,0,1,1,0]
result5=list(filter(lambda seat: seat==0 ,seats)),list(map(lambda s: "Available" if (s==0) else "Ocupied",seats))
print(list(result5))

# result6=map(lambda s: "Available" if (s==0) else "Ocupied",result5)
# print(list(result6))



    