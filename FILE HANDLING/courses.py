# Q.10 Course Fee Collection

with open("courses.csv","w") as file :
    file.write("Flutter,7000\n")
    file.write("Java,5000\n")
    file.write("Python,6000\n")
    file.write("React,8000")

with open("courses.csv","r") as file :
    print(file.read())
    file.seek(0)
    fees=0
    for line in file :
       data=line.strip().split(",")
       fees+=int(data[1])
print("Total Fee Collection :",fees)