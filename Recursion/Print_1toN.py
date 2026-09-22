# Write Function to print 1 to n
def Print_1toN(n):
  if n==0:
    return 0

  # Recursive Call : n to 1 then print 1 to n
  Print_1toN(n-1)

  # Print n
  print(n)

n=int(input("Enter value of n : "))
Print_1toN(n)