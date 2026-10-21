# finally : The finally block executes whether the opeartions succeds or raise an exception

try:
  number=int(input("Enter number"))
  result=number//0
except ZeroDivisionError:
  print("Cannot Divide by zero")
except ValueError:
  print("Invalid input")
else:
  print("Result",result)
finally:
  print("Program Executes finished!!!")