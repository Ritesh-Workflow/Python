# # Mobile Recharge Calculator
# # A recharge shop wants to calculate total recharge amount.
# # Given Data:
# # recharge1 = 199
# # recharge2 = 299
# # recharge3 = 149
# # Perform the following:
# # Create a function with parameters.
# # Accept recharge amounts.
# # Calculate total amount.
# # Return total amount.
# # Print returned value outside function.

# def recharge_calculator(rechareg1,recharge2,recharge3):
#     total_Amt=rechareg1+recharge2+recharge3
#     return total_Amt
# recharge=recharge_calculator(199,299,149)
# print("Total Amount :", recharge)



# #Employee Attendance System
# # A company wants to print employee details.
# # Given Data:
# # name = Ramesh
# # department = HR
# # salary = 25000
# # Perform the following:
# # Create a function with multiple parameters.
# # Print all employee details.
# # Call function using positional arguments.
# # Call function again using keyword arguments.
# # Observe argument sequence behavior.

# def employee_Details(name,department,salary):
#     print(f"Name :{name}")
#     print(f"Department :{department}")
#     print(f"Salary :{salary}")

# employee_Details("Ramesh","HR",25000)
# print("=========================")
# employee_Details(department="HR",salary=25000,name="Ramesh")



# # Electricity Bill Generator
# # An electricity office wants to generate bill amount.
# # Given Data:
# # units = 145
# # price_per_unit = 8
# # Perform the following:
# # Create a function with return type.
# # Calculate total bill.
# # Return bill amount.
# # Print final bill.
# # Display high bill message if amount exceeds 1000.

# def bill_Generator(units,price_per_unit):
#     total=units*price_per_unit
#     if total>1000:
#         print("High Bill")
#     return total
# bill=bill_Generator(145,8)
# print(bill)



# # #College Information System
# # A college wants default city name if user does not provide it.
# # Given Data:
# # college_name = MIT College
# # default_city = Pune
# # Perform the following:
# # Create a function with default argument.
# # Print college name and city.
# # Call function without city argument.
# # Call function with custom city.
# # Compare outputs.

# def collage_info(college_name,city="Pune"):
#     print(f"College Name :{college_name}")
#     print(f"College City :{city}")

# collage_info("MIT Colleg")
# collage_info("GECA","Chh.Sambhajinagar")



# # Online Shopping Discount Checker
# # An online store wants to check discount eligibility.
# # Given Data:
# # amount = 4500
# # Perform the following:
# # Create a function with parameter.
# # Check if amount is greater than 3000.
# # Print discount available message.
# # Otherwise print no discount.
# # Return final amount.

# def discount_checker(amount):
#     if amount>3000:
#         print("Discount Available")
#     else:
#         print("NO Discount")
#     return amount
# print(discount_checker(500))



# # Hospital Patient Details
# # A hospital wants to store patient information dynamically.
# # Given Data:
# # name = Amit
# # age = 45
# # disease = Fever
# # room = 204
# # Perform the following:
# # Create a function using **kwargs.
# # Accept dynamic patient details.
# # Print all key-value pairs.
# # Use loop for displaying data.
# # Print total number of details entered.

# def patient_Info(**kwargs):
#     for key,value in kwargs.items():
#         print(f"{key} = {value}")
#     print(f"Total number of details :{len(kwargs)}")
#     print(kwargs.items())
    
# patient_Info(name="Amit",age=25,room=204)

def outerfun():
    print("Hello")
    def inner():
        print("Bye")
        return "inner"
    return inner()
outerfun()

