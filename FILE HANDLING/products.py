# Q.2 Product Stock Manager 

file=open("products.txt","w")
file.write("P101,Laptop,10\n")
file.write("P102,Mouse,25\n")
file.write("P103,Keyboard,15\n")
file.write("P104,Monitor,8")
file.close()

file=open("products.txt","r")
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())

file.seek(0)
stock=0
for line in file:
    data=line.strip().split(",")
    stock+=int(data[2])
print("Total Stock :",stock)

