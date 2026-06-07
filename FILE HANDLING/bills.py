# Q.5 Coustomer Bill Generator

file=open("bills.txt","w")
file.write("C101,2500\n")
file.write("C102,3200\n")
file.write("C103,1500\n")
file.write("C104,4000")
file.close()

file=open("bills.txt","r")
amt=0
for line in file :
    print(line)
    data=line.strip().split(",")
    amt+=int(data[1])
print("Total Collection Amount :",amt)