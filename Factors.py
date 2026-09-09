n=int(input("Enter number "))


counter=2
while counter < n-1:
  if n%counter==0:
    print(counter)
  counter=counter+1