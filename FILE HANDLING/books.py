# Q.8 Book Library Record

try :
    file=open("books.txt","x")
    file.write("B101,Python Basics\n")
    file.write("B102,Java Fundamentals\n")
    file.write("B103,C Programming\n")
    file.write("B104,Flutter Development\n")

except FileExistsError as e:
    print(e)

finally :
    file=open("books.txt","r")
    print(file.read())
    file.seek(0)
    count=0
    for line in file :
        count+=1
    print('Total Books :',count)

