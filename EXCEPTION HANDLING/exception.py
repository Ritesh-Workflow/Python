# try:
#     print("Try Block")


# except:
#     print("Except Block")


# print("Exception Program...")
# num = int(input("Enter a number :"))
# print(num)

# print("After exception")


#try:
    # print("Exception Program...")
    # num = int(input("Enter a number :"))
    # print(num)
    # print(50/num)


#     names = ["Ashutosh" , "Sagar" , "Amol"]
#     print(names[3])

#     data = {
#         "name" : "Sanjay"
#     }
    
#     print(data["name"])


# except ValueError:
#     print("Wrong input entered")

# except ZeroDivisionError:
#     print("You cannot use zero value.")

# except IndexError:
#     print("Entered index out of bound....!")

# except Exception as e:
#     print("Error is : ", e)

# else:
#     print("Within a else block")

# finally:
#     print("Within a finally block.")

# print("After exception")



# Raise ---> Custom Error throw


# class InvalidAgeException(Exception):
#     pass

# try:

#     age = int(input("Enter age :"))

#     if age <= 18:
#         print("value less than 18...")
#         raise InvalidAgeException("Age must be 18 or above.")
#     else:
#         print("within else block")


# except InvalidAgeException as e:
#     print("Value error : " , e)




# Q.1 Student Percentage Calculator

# try :
#     student_name=input("Enter Student Name :")
#     marks_obtained=int((input("Enter Obtained Marks :")))
#     max_marks=int(input("Enter Maximum Marks :"))

#     percentage=(marks_obtained/max_marks)*100
#     print(f"{student_name} Got {percentage}%") 

# except ValueError: 
#     print("You Entered text instead of number")

# except ZeroDivisionError:
#     print("You Entered 0")




# Q.2 Reading Room Seat Lookup

try :
   seats=[101,102,103,104,105]
   position=int(input("Enter a Seat Position : "))
   print(f"Seat Number {seats[position]}")

except ValueError:
   print("You entered a text")

except IndexError :
   print(f"Seat Are not Available at {position} ")

finally :
   print("Program Succesfully Executed")