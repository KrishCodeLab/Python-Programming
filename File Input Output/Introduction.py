# Input: Getting data from a file into your Python program.
# Output: Sending data from your Python program into a file.

# workflow :  open file -> perforom some operations on file -> close file -> file operation completed

# Types of files : 
# text files - > .txt,.docs,.log etc
# binary files -> .mp4,.mov,.png,.jpg etc

# open file : We have to open a file before reading or writing
# f=open("file name ","mode") 

# Write content in opend file
file=open("personal.txt","w")
file.write("Name : Krushna Rajesh Govardhane\n")
file.write("Age: 20\n")
file.write("Course: B.Tech CSE")

file.close()

# Read content of opend file
file=open("personal.txt","r")
# read() : Read entire content of the file
content= file.read()
print(content)

file.close()

# readline() : Read one line of content
file=open("personal.txt","r")
line1=file.readline()
line2=file.readline()
line3=file.readline()
print(line1)
print(line2)
print(line3)

file.close()

# readlines() : Reads all lines and returns them as a list.
file=open("personal.txt","r")
content=file.readlines()
print(content)
file.close()