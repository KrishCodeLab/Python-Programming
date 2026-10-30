# KBC - Quiz Game
# Architecture of the project : 1->Welcome the player. 2->Ask the player's name. 3->Display a question. 4->Show four options.
# 5-> Take the player's answer. 6->Check whether the answer is correct. 7->Increase prize money if correct. 8->Stop the game if incorrect.
# 9->Display the final winning amount.


# Welcoming user
print("================================")
print("WELCOME TO KBC GAME")  
print("================================")


print("Welcome to Kaun Banega Crorepati!")

# Taking user name and printing start game message
name=input("What's your good name ? ")
print(f"Welcome {name} let's start game !!! ")
amount=0

Quiz={
  "question":"What is financial capital of india ?",
  "Options":["Delhi","Bengloare","Pune","Mumbai"],
  "answer":"D",
  "amount":100000
}

print(Quiz["question"])
option_list="ABCD"

# Printing Options
# Why Enumerate ? Enumerate enumerate() is a Python built-in function that gives you two things while iterating:
# 1. Index – Position of an element.
# 2. Value – Actual element.
for i, option in enumerate(Quiz["Options"]):
    print(f"{option_list[i]} : {option}")

anwser=input("Enter Option (A/B/C/D)").upper()
if anwser not in  option_list:
   print("Invalid Answer")

elif anwser==Quiz["answer"]:
   print("Correct Answer!")
   amount += Quiz["amount"]
   print(f"You won Rs. {amount}")
else:
   print("Incorrect Answer")
   print("Game is over")
  #  print(f"You won Rs. {amount}")


# Final result
print("\n================================")
print(f"Your final winning amount: Rs. {amount}")
print("================================")