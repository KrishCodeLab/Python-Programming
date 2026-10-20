# For else : After loop executed without encountering a break the else statement always executes.

for i in range(10):
  print(i)
else:
  print("Number 10 can't print")


for i in range(10):
  print(i)
  if i==5:
    break
else:
  print("loop executed successfully")

counter=1
while counter <= 10:
  print(counter)
  counter+=1
else:
  print("While loop executed")

# Example :
numbers = [10, 20, 30, 40]
target = 30

for num in numbers:
    if num == target:
        print("Number found!")
        break
else:
    print("Number not found!")