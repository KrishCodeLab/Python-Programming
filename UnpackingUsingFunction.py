# Unpacking Collection using function

def calculate(a,b):
  sum=a+b
  sub=a-b
  mul=a*b
  div=a/b
  return (sum,sub,mul,div)

addition,subtraction,multiplication,division=calculate(100,10)
print("Addition :",addition)
print("Subtraction :",subtraction)
print("Multiplication :",multiplication)
print("Division :",division)
