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
Amount=0

Quiz={
  "question":"What is financial capital of india ?",
  "Options":["Delhi","Bengloare","Pune","Mumbai"],
  "answer":"Mumbai",
  "amount":100000
}

print(Quiz["question"])
string="ABCD"
for i in string:
  print(f"{i} : {Quiz["Options"]}")

anwser=input("Enter your answer")
if Quiz["answer"]==anwser:
  print("Good Go To Next")
  Amount=Amount+int(Quiz["amount"])
print("Yow won ",Amount)
