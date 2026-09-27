# Check Whether string is palindrome or not
word=input("Enter word")
length=len(word)
s=""
for i in range(length-1,-1,-1):
  print(word[i],end="")
  s+=word[i]

print()
if word==s:
  print("The String is Palindrome")
else:
  print("The String is not Palindrome")