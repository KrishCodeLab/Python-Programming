# with statement : Python automatically closes the file when execution leaves the with block, even if an exception occurs.

with open("student.txt","r") as file:
  content=file.read()
  print(content)

# Without with	              With with
# Manual closing required	  Automatically closes
# More code	                Cleaner code
# Easier to forget closing	Safer resource management

# close stement with error
# workflow --> Open file -> write -> result = 10/0 stops execution. 
file = open("student.txt", "w")

file.write("Name: Krish\n")

# result = 10 / 0

file.write("Age: 20")

file.close()

print("File closed successfully")


# Using finally close the file : After error occured finally block executes close statement.
file = open("student.txt", "w")

try:

    file.write("Name: Krish\n")

    # result = 10 / 0

    file.write("Age: 20")

finally:

    file.close()

print("File closed successfully")

# Cleaner approach for file close 
with open("student.txt", "a") as file:

    file.write("Role:AI Scientist")
    