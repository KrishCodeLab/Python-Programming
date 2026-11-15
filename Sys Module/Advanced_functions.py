# Command Line Argument : It is very important and useful property or advantage of sys module.Command line argument means running your program on terminal using command like main.py 
# suppose in case you want to pass argument while executing code like
# main.py Krish 20 here main.py is the file and Krish and 20 are arguments.
import sys
print(sys)

# sys.argv --> It is list containing command-line arguments passed to your Python program.
print(sys.argv)


# Accessing individual argument
Name=sys.argv[1]
age=sys.argv[2]
role=sys.argv[3]

print("Name : ",Name)
print("age : ",age)
print("Role : ",role)

# exit() : Sometimes you want to stop the program execution immediatly.
print("The program is running ")

print("The program is going to stop ")
sys.exit()
print("The program is stopped")
# sys.exit() raises the SystemExit exception, which normally terminates the program.

# using exit codes : 0 for successful execution and non zero value for error
if age < 18:
  print("Access denied !")
  sys.exit(1)
else:
  print("Access Granted !")