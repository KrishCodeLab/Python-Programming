# Right Angled Numbered Pyramid 2

n=int(input("Enter value of n: "))

# Time Complexity - O(n2)
# outer loop for number of rows 
for i in range(1,n+1):
  # inner loop for each and every number 
  for i in range(1,i+1):
    print(i,end=" ")
  print()