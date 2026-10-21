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



# if loop terminate by break still else block will print
try:
  for i in range(11):
    print(i)
    if i==5:
      break
except ValueError:
  print("ValueError Happens")
else:
  print("Sorry !!!")
