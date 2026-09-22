# Print Even numbers
def PrintEven(n):
  if n==1 or n==0:
    return 0

  # Recursive Call
  PrintEven(n-1) # To calculate even numbers 100 to 2 and after that started printing from 2 to 100

  # Calculate Even Numbers from 2 to 100
  if n%2==0:
    print("Even Number",n)
  
  



n=int(input("Enter value of n : "))
PrintEven(n)