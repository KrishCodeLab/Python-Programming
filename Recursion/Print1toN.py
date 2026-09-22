
def Print1toN(n):
# Base condition
  if n==0:
    return 0;
  print(n) #n=5,4,3,2,1,
  Print1toN(n-1)
  


n=int(input("Enter value of n : "))
Print1toN(n)
