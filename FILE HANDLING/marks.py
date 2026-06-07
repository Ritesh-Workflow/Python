# Q.4 Student Mark Analyzer 

file=open("marks.txt","w")
file.write("101,Ritesh,78\n")
file.write("102,Kashish,85\n")
file.write("103,Ashutosh,91\n")
file.write("104,Manoj,66")
file.close()

file=open("marks.txt","r")
print(file.read())
file.seek(0)
total_marks=0
for line in file :
    data=line.strip().split(",")
    total_marks=total_marks+int(data[2])
print("Total Marks :",total_marks)
print("Average Marks :",total_marks/4)
file.close()