# write
file=open("student.txt","w")
file.write("Name : Krushna Rajesh Govardhane \n")
file.write("Age : 20 \n")
file.write("Course : B.Tech in CSE AI")


file.close();


# read

# read() reads the entire file and moves the file pointer to the end.
# When readline() executes, there is nothing left to read.
# Similarly, readlines() also finds nothing remaining.
file=open("student.txt","r")

# content=file.read()

# line1=file.readline()
# line2=file.readline()
all_lines=file.readlines()
print(all_lines)

# print(content)
# print(line1)
# print(line2)
file.close()


# Append
file=open("student.txt","a")
new_content="\n Google SDE  Developer"
file.write(new_content)

file.close()

# Read again
file=open("student.txt","r")
content=file.read()
print(content)

file.close()
