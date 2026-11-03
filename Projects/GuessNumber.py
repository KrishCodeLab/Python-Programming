import random

# Guess Random Number
random_number=(random.random()*100+1).__floor__()
chances=int(input("Enter how many chances you want to guess number "))
guess=int(input("Enter Guess "))

print(random_number)
while chances > 0:
  # check if guess is string
   if guess > random_number:
      print("Guess is Greater... Guess smaller one")
      guess=int(input("Enter Guess "))
   elif guess < random_number:
      print("Guess is Smaller... Guess Greater one")
      guess=int(input("Enter Guess "))
   elif guess==random_number:
      print(f"Congratulations You Gussessed correct number {random_number}")
      print(f"You guessed number in {chances} chances")
      break
   chances -=1
    
   