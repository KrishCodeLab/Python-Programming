
# Write Fucntion print Odd Numbers using Recursion

def PrintOdd(n):
  if n==0:
    return 1

  # Recursive call
  PrintOdd(n-1) #100 to 1 recusive call then will start printing from 2 to 100

  #Printing Odd Numbers 1 to 100
  if n%2==1:
    print("Odd Number ",n)

n=int(input("Enter value of n : "))
PrintOdd(n)