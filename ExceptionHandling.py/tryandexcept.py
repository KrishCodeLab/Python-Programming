# What is Exception Handling in Python ? 
# Exception handling is a way to handle runtime errors so that your program can respond gracefully instaed of crashing unexpectedly.


# try : Contains code that might raise an exception.

# except : Handles an exception raised in the try block

try:
  number=int(input("Enter a number"))
  print(number/0)
except ZeroDivisionError:
  print("Number cannot be divided by zero")


try:
  num=int(input("Enter a number"))
  string=input("Enter a string")
  result=num+string
except TypeError:
  print("You can't add number into string")

try:
    age = int("hello")
    print(age)

except ValueError:
    print("Invalid value! Enter a number.")


try:
    numbers = [10, 20, 30]
    print(numbers[5])

except IndexError:
    print("List index is out of range!")