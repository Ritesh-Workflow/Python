# Q.9 Mobile Sales Report

file=open("sales.txt","w")
file.write("Samsung,5\n")
file.write("Vivo,3\n")
file.write("Oppo,4\n")
file.write("Realme,6\n")
file.close()

file=open("sales.txt","r")
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
file.seek(0)
sold=0
for line in file :
    data=line.strip().split(",")
    sold+=int(data[1])
print("Total Mobiles Sold :",sold)

file=open("sales.txt","a")
file.write("Motorola,1")
file.close()

file=open("sales.txt","r")
print(file.read())