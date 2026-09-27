# Count number of Vowels in string
s=input("Enter String ")
length=len(s)
count=0
for i in range(0,length):
  if s[i]=='a':
    count=count+1
  elif s[i]=='e':
    count=count+1
  elif s[i]=='i':
    count=count+1
  elif s[i]=='o':
    count=count+1
  elif s[i]=='u':
    count=count+1
  else:
    pass
print("Number of vowels : ",count)