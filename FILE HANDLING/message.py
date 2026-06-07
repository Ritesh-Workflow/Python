# Q.6 Pointer Position Checker
file=open("message.txt","w")
file.write("Welcome to Python File Handling")

file=open("message.txt","r")
print(file.read(10))
print(file.tell())
file.seek(5)
print(file.read())