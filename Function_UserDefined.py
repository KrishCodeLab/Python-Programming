# User Defined Functions
def sayHello():
  print("Hello!!!")

def sayHii():
  print("Hii!!")

def sayNamste():
  print("Namaste!!!")


sayHello()
sayHii()
sayNamste()


# Default Parameter - Assigning a default value to parameters, which is used when no argument is passed

def calc_sum(a=5,b=1):
  return a+b

def calc_sub(a=5,b=1):
  return a-b

def calc_mul(a=5,b=1):
  return a*b

def calc_div(a=5,b=2):
  return a/b

print("Sum of default values =",calc_sum()) #call function without arguments then function will use default values
print("Sub of default values =",calc_sub()) 
print("Mul of default values =",calc_mul()) 
print("Div of default values =",calc_div()) 

a=10
b=20

print("Sum of two arguments",calc_sum(a,b)) #call function with argument then function wil perform operation on them
print("Sub of two arguments",calc_sub(a,b))
print("Mul of two arguments",calc_mul(a,b))
print("Div of two arguments",calc_div(a,b))