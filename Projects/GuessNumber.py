import random

# Guess Random Number
random_number=(random.random()*100+1).__floor__();
guess=int(input("Enter Guess "))
print(random_number)
while True:
  # check if guess is string
   if guess > random_number:
      print("Guess is Greater... Guess smaller one")
      guess=int(input("Enter Guess "))
   elif guess < random_number:
      print("Guess is Smaller... Guess Greater one")
      guess=int(input("Enter Guess "))
   elif guess==random_number:
      print(f"Congratulations You Gussessed correct number {random_number}")
      break
   
    
   