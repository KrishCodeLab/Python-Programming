import random

# random.choice()
# Selects one random element from a sequence (such as a list, tuple, or string).

sequence=[1,3,4,5,6,7,9]
choice=random.choice(sequence)
print(choice)

for i in range(len(sequence)):
  choice=random.choice(sequence)
  print("Random element from sequence",choice)


fruits=("Mango","Apple","Pineapple","Papaya","Orange")
for i in range(len(fruits)):
  choice=random.choice(fruits)
  print("Random fruit from sequence",choice)