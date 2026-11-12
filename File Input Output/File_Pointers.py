# When you read the first page, your position moves forward. Similarly, Python maintains a position inside an opened file.
# This position is called the file pointer or file position

with open("student.txt","a") as file:
  file.write("\nCourse: B.Tech CSE AI")
  file.write("\nRole:AI Scientist")

# tell() : Returns current file position
with open("student.txt","r") as file:
  print("Current file position",file.tell())
  content=file.read()
  print(content)
  print("Current file position",file.tell())

# seek() : Moves the file position to a specified location.
with open("student.txt","r") as file:
  content=file.read(4)
  print(content)
  print(file.seek(0))
  print(file.read(4))

# seek(offset,whence) : seek with parameters
# offset : Number of bytes/positions to move.
# whence : 0-->Starting of the file  1-->Current position of file  2-->End of the file
with open("student.txt", "rb") as file:

    file.seek(5, 0)
    print(file.tell())  # 5

    file.seek(3, 1)
    print(file.tell())  # 8

    file.seek(-2, 2)
    print(file.tell())  # 247-2 = 245

# writelines() : We already learn write() that is used for write string , similarly writelines() is used to write multiple strings from an iterable
    
students = [
    "Krish\n",
    "Rahul\n",
    "Amit\n",
    "Rohan\n"
]

with open("students.txt", "w") as file:
    file.writelines(students)

with open("students.txt","r") as file:
   print(file.read())