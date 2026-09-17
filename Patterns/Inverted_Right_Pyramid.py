# Inverted Right Pyramid 
n =int(input("Enter value of n : "))



# Time Complexity - O(n2)
# outer loop for number of rows
# Printing Inverse Pattern so simply started with n ,then set range n to 0 
for i in range(n,0,-1):
  # inner loop for printing each and every number
  for j in range(1,i+1):
    print(j,end=" ")
  print()