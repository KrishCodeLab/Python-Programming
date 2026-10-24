# Enumerator Function 
# The enumerate() function in Python is used to get both the index and the value of each element while looping through a sequence such as a list, tuple, or string.

n=["krishna","krish","kishu","krushna",]
index=0
for mark in n:
  print(mark)
  if index==3:
    print(index)
  index +=1
print("End")


name = "Python"

for index, character in enumerate(name):
    print(index, character)


subjects = ["Python", "Java", "SQL"]

for index, subject in enumerate(subjects, start=1):
    print(index, subject)