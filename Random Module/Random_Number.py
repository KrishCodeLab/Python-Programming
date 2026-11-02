import random

fruits=["Mango","Banana","Apple","Pineapple","Papaya","Orange"]
length=len(fruits)
random_number=random.random()*100+1
print(random_number)
# floor function is used to round the number
print(random_number.__floor__())