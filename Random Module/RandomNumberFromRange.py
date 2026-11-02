import random

# Geneartes random number between 1 to 100
n=random.randint(1,100)
print(n)

# Assign Roll Numbers Randomly
for i in range(1,100+1):
  roll_n=random.randint(1,100)
  print("Roll No. of student is ",roll_n)

# What is difference between randint and randrange
# Feature	randint()	randrange()
#  Start	Inclusive	Inclusive
#  Stop	  Inclusive	Exclusive
#  Step   	No	      Yes
#  Arguments	2	    1, 2 or 3


# Print positive integers
for i in range(1,101):

  num=random.randrange(0,100,2)
  print(num)

