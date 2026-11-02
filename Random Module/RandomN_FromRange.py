import random

fruits=["Mango","Banana","Apple","Pineapple","Papaya","Orange"]
# Calculating Range to find random number 0 to len of list
length=len(fruits)
# Using randrange() generating random number
random_idx=random.randrange(length)
# Printing the random item using random idx
print(fruits[random_idx])

