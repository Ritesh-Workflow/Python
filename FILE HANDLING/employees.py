# Q.1 Employee Salary Report

file=open("employees.txt","w")
file.write("101,Rahul,25000\n")
file.write("102,Amit,30000\n")
file.write("103,Priya,28000\n")
file.write("104,Neha,35000\n")
file.close()

file=open("employees.txt","r")
print(file.read())
file.close()
file=open("employees.txt","r")

salary=0
for line in file :
       data=line.strip().split(",")
       print(data[2])
       salary=salary+int(data[2])
print("Total Salary :",salary)