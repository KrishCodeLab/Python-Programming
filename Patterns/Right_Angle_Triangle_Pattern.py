# Right Angle Triangle Pattern
n=int(input("Enter value of  n : "))

# Optimized Approach - Time Complexity O(n)
for i in range(1,n+1):
  print("* "*i)

print()
print()


# Brute Force Approach - Time Complexity O(n2)
for i in range(1,n+1):

  for j in range(1,i+1):
    print("*",end=" ")

  print()