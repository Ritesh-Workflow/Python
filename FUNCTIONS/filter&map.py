# MAP() & FILTER() FUNCTIONS



# QR Code ID Generator
# A library wants to generate unique QR IDs for students
# student_ids = [101, 102, 103, 104]
# updated_id=list(map(lambda id: "LIB-"+str(id),student_ids))
# reverse_id=list(map(lambda id: id[::-1],updated_id))
# count=len(reverse_id)
# print(updated_id)
# print(reverse_id)
# print("Total IDs Generated : ",count)



# Seat Number Formater
# A reading room app wants seat numbers in a formated way
# seats=[1,2,3,4,5]
# formatted_seats=list(map(lambda seat: "seat-"+(str(seat)),seats))
# longest_string=max(formatted_seats, key=len)
# print(longest_string)
# print(formatted_seats)
# total_char=0
# for char in formatted_seats:
#     total_char=len(char)+total_char
# print(f"Total Characters : {total_char}")



# File Extension creater
# files = ["receipt", "invoice", "report", "summary"]
# new_files=list(map(lambda file: file+".pdf",files))
# uppercase=list(map(str.upper,new_files))
# sortedfiles=sorted(uppercase)
# print(f"New Files : {new_files}")
# print(f"Upper Case : {uppercase}")
# print(f"Sorted File Names : {sortedfiles}")



# Student Email Creator
# students=["Rahul","Priya","Amit","Sneha"]
# students_email=list(map(lambda name : name.lower()+"@gmail.com",students))
# print(students_email)
# letter_a=list(filter(lambda x : "rahul" in x,students_email))
# print(letter_a)



# Delivery Tracking Numbers 
orders=[5001,5002,5003]
tracking_id=list(map(lambda order: "TRK"+str(order),orders))
print(tracking_id)
numeric_part=list(filter(lambda id: id[3],tracking_id))
print(numeric_part)