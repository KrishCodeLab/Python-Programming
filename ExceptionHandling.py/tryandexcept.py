# What is Exception Handling in Python ? 
# Exception handling is a way to handle runtime errors so that your program can respond gracefully instaed of crashing unexpectedly.


# try : Contains code that might raise an exception.

# except : Handles an exception raised in the try block

try:
  number=int(input("Enter a number"))
  print(number/0)
except ZeroDivisionError:
  print("Number cannot be divided by zero")