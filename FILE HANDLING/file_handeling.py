# File Writing

# file = open("students.txt","w")

# file.write("101,Ashutosh,5000\n")
# file.write("102,Kashish,4000\n")
# file.write("103,Ritesh,550\n")
# file.write("104,Ritesh,5500\n")

# file.close()

# File reading

file = open("students.txt", "r")

# print(file.read())
# print(file.read(16))
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())

# file.close()


# file = open("students.txt" , "a")

# file.write("105,Avinash,9000\n")

# print("Position of pointer : " , file.tell())

# file.close()

# file=open("students.txt" , "r")
# print("----")
# file.seek(40)
# print("----")

# print(file.read())

# file.close()

# # With open


# with open("students.txt" , "r") as file:
#     print(file.read())


# with open("students.txt" , "a") as file:
#     file.write("NEW DATA ADDED\n")

# try:
#     with open("student_info.csv", "x") as file:
#         # file.write("name,age,fees\n")
#         file.write("Ritesh,20,3000\n")
#         file.write("Kashish,20,5000\n")
#         file.write("Ashutosh,20,7000\n")
#         file.write("Manoj,20,9000\n")

# except FileExistsError as e:
#     print(e)

# finally:
#     with open("student_info.csv", "r") as file:
#         amount = 0
#         for line in file:
#             data = line.strip().split(",")
#             print(data[2])
#             amount = amount + int(data[2])
#         print("Total Fees : ", amount)