# Q.7 Attendance Record
file=open("attendance.txt","w")
file.write("Rahul,Present\n")
file.write("Priya,Absent\n")
file.write("Amit,Present\n")
file.write("Neha,Present")

file=open("attendance.txt","r")
print(file.read())
file.seek(0)
count=0
for line in file :
    data=line.strip().split(",")
    if data[1]=="Present":
        count+=1

print("Total Present Students :",count)