# Reverse a Number
n=int(input("Enter value of n : "))
s=str(n)

for i in range(len(s)-1,-1,-1):
  print(s[i],end="")

