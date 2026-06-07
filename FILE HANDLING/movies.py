# Q.3 Movie Collection

file=open("movies.txt","w")
file.write("M101,KGF,8.5\n")
file.write("M102,Pushpa,8.1\n")
file.write("M103,Kantara,9.0\n")
file.write("M104,Leo,7.9\n")
file.close()

file=open("movies.txt","r")
print(file.read())
file.close()

file=open("movies.txt","a")
file.write("M105,PK,9.4")
file.close()
file=open("movies.txt","r")
print(file.read())
file.close()
