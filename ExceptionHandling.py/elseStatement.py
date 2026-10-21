# else in exception handling : Executes when the try block completed without an exception
try:
  num=int(input("Enter a number"))
  d=int(input("Enter a  number"))
  result=num/d
except ZeroDivisionError:
  print("The number must be greater than 0 ")
else:
  print("hello")
  print(result)