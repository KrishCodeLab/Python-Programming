# Write function to print factorial of n using Recursion
def factorial(n):
  if n==0:
    return 1

  # factorial(n-1) # Calculating numbers from n to 1 and started perfoming operation from 1 

  # Calculate and  Print Factorial
  
  return n*factorial(n-1) 

n=int((input("Enter value of n : ")))
print(factorial(n))