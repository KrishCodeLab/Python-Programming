# Print fact of n

def factorial(n):
  fact=1
  counter=1
  while(counter <= n):
    fact=fact*counter
    counter=counter+1
  return fact

n=int(input("Enter n "))
print(factorial(n))