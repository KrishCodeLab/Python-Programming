# Write a function to print n to 1

def PrintNto1(n):
# Base Condition
  if n==0:
    return 0

  # Print n
  print(n)
  # Recursive Call
  PrintNto1(n-1) #Second step :  n to 1 by Recursive call after that started printing from n to 1
  

n=int(input("Enter value of n : "))
PrintNto1(n)