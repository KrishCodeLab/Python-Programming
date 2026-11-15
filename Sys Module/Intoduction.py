# What is sys ? : Sys module is a built modul that provides access to variables and functions used to interact with python interpreter.
# It is used to interact with python interpreter.Python interpreter is the software that executes your python code.
# Use of Sys module
#  Get Python version information.
#  Access command-line arguments.
#  Exit a Python program.
#  Find the module search paths.
#  Get the current recursion limit.
#  Inspect memory size of objects.
#  Work with standard input and output.
#  Understand how Python handles imported modules.

import sys
print(sys)

# sys.version -> It is used to check python version that is installed in your system.
print("Python Version : ")
print(sys.version)

# sys.version_info --> It is similar like version but instead of just providing python version it provides more information about the python.
print("Python Version Information :")
print(sys.version_info)

# example :

if sys.version_info >= (3, 10): #In condtion 3 is the major version and 10 is minor version information.
    print("Python version supported")
else:
    print("Please upgrade Python")

# sys.executable :This returns the absoulte path of the python interpreter executable currently running your program.
print(sys.executable)