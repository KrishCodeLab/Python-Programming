# Find the longest word in a sentence.
sentence=input("Enter String here : ")
each_word=""
length=len(sentence)

word=""
longest=""
for i in range(length):
  # checking each word in sentence using another loop
  char=sentence[i]
  if char!=" ":
    word=word+sentence[i]
  else:
    if len(word)>=len(longest):
      longest=word
      
    word=""


# Check the last word
if len(word) >= len(longest):
    longest = word
  
print(longest) 


