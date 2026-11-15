# Simple Calculator using Command line argument 
import sys

num1=float(sys.argv[1])
operator=sys.argv[2]
num2=float(sys.argv[3])

if operator=="+":
  print(num1+num2)
elif operator=="-":
  print(num1-num2)
elif operator=="*":
  print(num1*num2)
elif operator=="/":
  if num2 != 0:
    print(num1/num2)
  else:
    print("Zero Division Error")
else:
  print("Invalid Error")
  

