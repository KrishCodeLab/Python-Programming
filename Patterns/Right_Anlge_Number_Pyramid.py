# Right Angled Numbered Pyramid

n=int(input("Enter value of n : "))


# Time Complexity - O(n2)
# outer loop for number of rows
for i in range(1,n+1):
  # inner loop for each and every number
  for j in range(1,i+1):
    print(j,end=" ")
  print()