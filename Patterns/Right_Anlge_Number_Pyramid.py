# Right Angled Numbered Pyramid

n=int(input("Enter value of n : "))

for i in range(1,n+1):
  for j in range(1,i+1):
    print(j,end=" ")
  print()