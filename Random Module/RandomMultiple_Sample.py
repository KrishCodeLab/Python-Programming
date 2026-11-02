import random

numbers=[10,20,30,40,50,60,70,80,90,100,200,300,400,500,600,700,800,900,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000]
# Selecting multiple elements using sample
random_k_items=random.sample(numbers,10)

for i in random_k_items:
  print(i)

print()
print()

random.shuffle(numbers)
print(numbers)