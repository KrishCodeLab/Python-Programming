# KBC - Quiz Game
# Architecture of the project : 1->Welcome the player. 2->Ask the player's name. 3->Display a question. 4->Show four options.
# 5-> Take the player's answer. 6->Check whether the answer is correct. 7->Increase prize money if correct. 8->Stop the game if incorrect.
# 9->Display the final winning amount.
import random

# Welcoming user
print("================================")
print("WELCOME TO KBC GAME")  
print("================================")


print("Welcome to Kaun Banega Crorepati!")

# Taking user name and printing start game message
name=input("What's your good name ? ")
print(f"Welcome {name} let's start game !!! ")
amount=0
phone=input("Enter your phone number : ")
email=input("Enter your email id : ")
bank_account=input("Enter bank account number : ")


# Store Questions using Dictionary
# Quiz={
#   "question":"What is financial capital of india ?",
#   "Options":["Delhi","Bengloare","Pune","Mumbai"],
#   "answer":"D",
#   "amount":100000
# }

# Storing multiple Dictionaries in List
questions = [
    {
        "question": "What is the financial capital of India?",
        "options": ["Delhi", "Bengaluru", "Pune", "Mumbai"],
        "answer": "D",
        "amount": 1000
    },
    {
        "question": "Who developed Python?",
        "options": ["James Gosling", "Guido van Rossum", "Dennis Ritchie", "Elon Musk"],
        "answer": "B",
        "amount": 2000
    },
    {
        "question": "Which is the largest planet in our solar system?",
        "options": ["Earth", "Mars", "Jupiter", "Venus"],
        "answer": "C",
        "amount": 3000
    },
    {
        "question": "What is the national animal of India?",
        "options": ["Lion", "Elephant", "Tiger", "Leopard"],
        "answer": "C",
        "amount": 4000
    },
    {
        "question": "How many continents are there?",
        "options": ["5", "6", "7", "8"],
        "answer": "C",
        "amount": 5000
    },
    {
        "question": "Which gas do plants absorb?",
        "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"],
        "answer": "B",
        "amount": 6000
    },
    {
        "question": "Who is known as the Father of the Nation in India?",
        "options": ["Jawaharlal Nehru", "Mahatma Gandhi", "Sardar Patel", "B. R. Ambedkar"],
        "answer": "B",
        "amount": 7000
    },
    {
        "question": "Which is the longest river in India?",
        "options": ["Yamuna", "Godavari", "Ganga", "Narmada"],
        "answer": "C",
        "amount": 8000
    },
    {
        "question": "What is the currency of Japan?",
        "options": ["Dollar", "Yuan", "Won", "Yen"],
        "answer": "D",
        "amount": 9000
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Venus", "Mars", "Saturn", "Mercury"],
        "answer": "B",
        "amount": 10000
    },
    {
        "question": "What is the chemical symbol of Gold?",
        "options": ["Ag", "Au", "Fe", "Cu"],
        "answer": "B",
        "amount": 11000
    },
    {
        "question": "Who wrote the Indian national anthem?",
        "options": ["Bankim Chandra Chatterjee", "Rabindranath Tagore", "Sarojini Naidu", "Premchand"],
        "answer": "B",
        "amount": 12000
    },
    {
        "question": "Which is the smallest prime number?",
        "options": ["0", "1", "2", "3"],
        "answer": "C",
        "amount": 13000
    },
    {
        "question": "How many players are there in a cricket team?",
        "options": ["9", "10", "11", "12"],
        "answer": "C",
        "amount": 14000
    },
    {
        "question": "Which organ pumps blood in the human body?",
        "options": ["Lungs", "Brain", "Heart", "Kidney"],
        "answer": "C",
        "amount": 15000
    },
    {
        "question": "Which is the largest ocean?",
        "options": ["Atlantic", "Indian", "Arctic", "Pacific"],
        "answer": "D",
        "amount": 16000
    },
    {
        "question": "Who invented the telephone?",
        "options": ["Thomas Edison", "Alexander Graham Bell", "Nikola Tesla", "James Watt"],
        "answer": "B",
        "amount": 17000
    },
    {
        "question": "Which programming language is primarily used for Android development?",
        "options": ["Kotlin", "PHP", "Ruby", "Swift"],
        "answer": "A",
        "amount": 18000
    },
    {
        "question": "What is the capital of Maharashtra?",
        "options": ["Pune", "Nagpur", "Mumbai", "Nashik"],
        "answer": "C",
        "amount": 19000
    },
    {
        "question": "Which device is used to measure temperature?",
        "options": ["Barometer", "Thermometer", "Speedometer", "Hygrometer"],
        "answer": "B",
        "amount": 20000
    },
    {
        "question": "Who was the first Prime Minister of India?",
        "options": ["Mahatma Gandhi", "Jawaharlal Nehru", "Lal Bahadur Shastri", "Rajendra Prasad"],
        "answer": "B",
        "amount": 21000
    },
    {
        "question": "What is the full form of CPU?",
        "options": ["Central Processing Unit", "Computer Processing Utility", "Central Program Unit", "Control Processing Unit"],
        "answer": "A",
        "amount": 22000
    },
    {
        "question": "Which language is known as the language of the web?",
        "options": ["Python", "Java", "JavaScript", "C"],
        "answer": "C",
        "amount": 23000
    },
    {
        "question": "How many bones are there in an adult human body?",
        "options": ["200", "206", "210", "212"],
        "answer": "B",
        "amount": 24000
    },
    {
        "question": "Which is the highest mountain in the world?",
        "options": ["K2", "Kangchenjunga", "Mount Everest", "Makalu"],
        "answer": "C",
        "amount": 25000
    },
    {
        "question": "What is the national flower of India?",
        "options": ["Rose", "Sunflower", "Lotus", "Lily"],
        "answer": "C",
        "amount": 26000
    },
    {
        "question": "Which company created the Windows operating system?",
        "options": ["Apple", "Microsoft", "Google", "IBM"],
        "answer": "B",
        "amount": 27000
    },
    {
        "question": "Which vitamin is produced by the body with sunlight exposure?",
        "options": ["Vitamin A", "Vitamin B12", "Vitamin C", "Vitamin D"],
        "answer": "D",
        "amount": 28000
    },
    {
        "question": "What is the square root of 144?",
        "options": ["10", "11", "12", "14"],
        "answer": "C",
        "amount": 29000
    },
    {
        "question": "Which country is famous for the Eiffel Tower?",
        "options": ["Italy", "France", "Germany", "Spain"],
        "answer": "B",
        "amount": 30000
    },
    {
        "question": "Which data type is immutable in Python?",
        "options": ["List", "Dictionary", "Set", "Tuple"],
        "answer": "D",
        "amount": 31000
    },
    {
        "question": "What does HTML stand for?",
        "options": ["Hyper Text Markup Language", "High Text Machine Language", "Hyper Transfer Markup Language", "Home Tool Markup Language"],
        "answer": "A",
        "amount": 32000
    },
    {
        "question": "Who discovered gravity after observing a falling apple?",
        "options": ["Albert Einstein", "Isaac Newton", "Galileo Galilei", "Nikola Tesla"],
        "answer": "B",
        "amount": 33000
    },
    {
        "question": "Which is the fastest land animal?",
        "options": ["Lion", "Horse", "Cheetah", "Tiger"],
        "answer": "C",
        "amount": 34000
    },
    {
        "question": "What is the national bird of India?",
        "options": ["Parrot", "Peacock", "Eagle", "Swan"],
        "answer": "B",
        "amount": 35000
    },
    {
        "question": "Which protocol is used for secure web browsing?",
        "options": ["HTTP", "FTP", "HTTPS", "SMTP"],
        "answer": "C",
        "amount": 36000
    },
    {
        "question": "What is the boiling point of water at sea level?",
        "options": ["50°C", "75°C", "100°C", "150°C"],
        "answer": "C",
        "amount": 37000
    },
    {
        "question": "Which Indian city is known as the Pink City?",
        "options": ["Udaipur", "Jaipur", "Jodhpur", "Bhopal"],
        "answer": "B",
        "amount": 38000
    },
    {
        "question": "Which company developed the Android operating system initially?",
        "options": ["Apple", "Android Inc.", "Microsoft", "Nokia"],
        "answer": "B",
        "amount": 39000
    },
    {
        "question": "What is the value of pi approximately?",
        "options": ["2.14", "3.14", "4.14", "5.14"],
        "answer": "B",
        "amount": 40000
    },
    {
        "question": "Which is the largest desert in the world?",
        "options": ["Sahara", "Gobi", "Antarctic Desert", "Arabian Desert"],
        "answer": "C",
        "amount": 41000
    },
    {
        "question": "Which keyword defines a function in Python?",
        "options": ["function", "define", "def", "fun"],
        "answer": "C",
        "amount": 42000
    },
    {
        "question": "What is the full form of RAM?",
        "options": ["Read Access Memory", "Random Access Memory", "Run Access Module", "Random Application Memory"],
        "answer": "B",
        "amount": 43000
    },
    {
        "question": "Who was the first President of India?",
        "options": ["Dr. Rajendra Prasad", "Dr. A. P. J. Abdul Kalam", "S. Radhakrishnan", "Zakir Husain"],
        "answer": "A",
        "amount": 44000
    },
    {
        "question": "Which blood group is known as the universal red cell donor?",
        "options": ["AB+", "O+", "O-", "A-"],
        "answer": "C",
        "amount": 45000
    },
    {
        "question": "Which is the closest star to Earth?",
        "options": ["Sirius", "Sun", "Alpha Centauri", "Polaris"],
        "answer": "B",
        "amount": 46000
    },
    {
        "question": "Which method adds an element to the end of a Python list?",
        "options": ["insert()", "append()", "add()", "extend_one()"],
        "answer": "B",
        "amount": 47000
    },
    {
        "question": "Which Indian state is famous for tea gardens in Darjeeling?",
        "options": ["Assam", "Sikkim", "West Bengal", "Kerala"],
        "answer": "C",
        "amount": 48000
    },
    {
        "question": "Which metal is liquid at room temperature?",
        "options": ["Iron", "Mercury", "Aluminium", "Copper"],
        "answer": "B",
        "amount": 49000
    },
    {
        "question": "Which planet has prominent rings?",
        "options": ["Mars", "Earth", "Saturn", "Mercury"],
        "answer": "C",
        "amount": 50000
    },
    {
        "question": "What does SQL stand for?",
        "options": ["Structured Query Language", "Simple Question Language", "System Query Logic", "Sequential Query Language"],
        "answer": "A",
        "amount": 51000
    },
    {
        "question": "Which is the largest state in India by area?",
        "options": ["Madhya Pradesh", "Maharashtra", "Rajasthan", "Uttar Pradesh"],
        "answer": "C",
        "amount": 52000
    },
    {
        "question": "Which part of a plant conducts photosynthesis?",
        "options": ["Root", "Stem", "Leaf", "Flower"],
        "answer": "C",
        "amount": 53000
    },
    {
        "question": "Which Python operator is used for exponentiation?",
        "options": ["^", "**", "//", "%%"],
        "answer": "B",
        "amount": 54000
    },
    {
        "question": "Which sport is associated with Wimbledon?",
        "options": ["Football", "Cricket", "Tennis", "Badminton"],
        "answer": "C",
        "amount": 55000
    },
    {
        "question": "What is the capital of Australia?",
        "options": ["Sydney", "Melbourne", "Canberra", "Perth"],
        "answer": "C",
        "amount": 56000
    },
    {
        "question": "Which organ helps humans breathe?",
        "options": ["Heart", "Lungs", "Liver", "Kidneys"],
        "answer": "B",
        "amount": 57000
    },
    {
        "question": "Which data structure follows FIFO?",
        "options": ["Stack", "Queue", "Tree", "Graph"],
        "answer": "B",
        "amount": 58000
    },
    {
        "question": "Which Indian scientist is known as the Missile Man of India?",
        "options": ["C. V. Raman", "Homi Bhabha", "A. P. J. Abdul Kalam", "Vikram Sarabhai"],
        "answer": "C",
        "amount": 59000
    },
    {
        "question": "What does CSS stand for?",
        "options": ["Creative Style Sheets", "Cascading Style Sheets", "Computer Style System", "Colorful Style Syntax"],
        "answer": "B",
        "amount": 60000
    },
    {
        "question": "Which is the hardest natural substance?",
        "options": ["Gold", "Iron", "Diamond", "Quartz"],
        "answer": "C",
        "amount": 61000
    },
    {
        "question": "Which country hosted the 2024 Summer Olympics?",
        "options": ["Japan", "France", "Brazil", "China"],
        "answer": "B",
        "amount": 62000
    },
    {
        "question": "What does len() return in Python?",
        "options": ["Memory size", "Number of elements", "Data type", "Index"],
        "answer": "B",
        "amount": 63000
    },
    {
        "question": "Which river is known as the Dakshin Ganga?",
        "options": ["Krishna", "Kaveri", "Godavari", "Tapi"],
        "answer": "C",
        "amount": 64000
    },
    {
        "question": "Which is the smallest continent by land area?",
        "options": ["Europe", "Australia", "Antarctica", "South America"],
        "answer": "B",
        "amount": 65000
    },
    {
        "question": "Which function converts a string into an integer in Python?",
        "options": ["str()", "float()", "int()", "bool()"],
        "answer": "C",
        "amount": 66000
    },
    {
        "question": "Which is the national aquatic animal of India?",
        "options": ["Blue Whale", "Ganges River Dolphin", "Crocodile", "Turtle"],
        "answer": "B",
        "amount": 67000
    },
    {
        "question": "Who painted the Mona Lisa?",
        "options": ["Pablo Picasso", "Vincent van Gogh", "Leonardo da Vinci", "Michelangelo"],
        "answer": "C",
        "amount": 68000
    },
    {
        "question": "Which keyword is used to handle exceptions in Python?",
        "options": ["catch", "except", "error", "handle"],
        "answer": "B",
        "amount": 69000
    },
    {
        "question": "What is the capital of Canada?",
        "options": ["Toronto", "Vancouver", "Ottawa", "Montreal"],
        "answer": "C",
        "amount": 70000
    },
    {
        "question": "Which is the largest mammal?",
        "options": ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"],
        "answer": "B",
        "amount": 71000
    },
    {
        "question": "What is the output of 10 // 3 in Python?",
        "options": ["3.33", "3", "4", "1"],
        "answer": "B",
        "amount": 72000
    },
    {
        "question": "Which Indian festival is known as the Festival of Lights?",
        "options": ["Holi", "Eid", "Diwali", "Pongal"],
        "answer": "C",
        "amount": 73000
    },
    {
        "question": "Which layer protects Earth from harmful ultraviolet radiation?",
        "options": ["Troposphere", "Ozone layer", "Core", "Ionosphere"],
        "answer": "B",
        "amount": 74000
    },
    {
        "question": "Which Python method converts text to lowercase?",
        "options": ["lower()", "casefolding()", "small()", "down()"],
        "answer": "A",
        "amount": 75000
    },
    {
        "question": "Who founded Microsoft?",
        "options": ["Steve Jobs and Steve Wozniak", "Bill Gates and Paul Allen", "Larry Page and Sergey Brin", "Mark Zuckerberg"],
        "answer": "B",
        "amount": 76000
    },
    {
        "question": "Which is the national tree of India?",
        "options": ["Neem", "Peepal", "Banyan", "Mango"],
        "answer": "C",
        "amount": 77000
    },
    {
        "question": "Which planet is closest to the Sun?",
        "options": ["Venus", "Earth", "Mercury", "Mars"],
        "answer": "C",
        "amount": 78000
    },
    {
        "question": "Which Python collection does not allow duplicate elements?",
        "options": ["List", "Tuple", "Set", "String"],
        "answer": "C",
        "amount": 79000
    },
    {
        "question": "What is the full form of URL?",
        "options": ["Uniform Resource Locator", "Universal Reference Link", "Unified Resource Language", "Uniform Read Location"],
        "answer": "A",
        "amount": 80000
    },
    {
        "question": "Which Indian state is known as God's Own Country?",
        "options": ["Goa", "Kerala", "Himachal Pradesh", "Uttarakhand"],
        "answer": "B",
        "amount": 81000
    },
    {
        "question": "Which instrument measures atmospheric pressure?",
        "options": ["Thermometer", "Barometer", "Anemometer", "Seismograph"],
        "answer": "B",
        "amount": 82000
    },
    {
        "question": "Which data structure follows LIFO?",
        "options": ["Queue", "Stack", "Linked List", "Graph"],
        "answer": "B",
        "amount": 83000
    },
    {
        "question": "Who wrote the Ramayana?",
        "options": ["Ved Vyasa", "Valmiki", "Kalidasa", "Tulsidas"],
        "answer": "B",
        "amount": 84000
    },
    {
        "question": "What is the binary representation of decimal 5?",
        "options": ["100", "101", "110", "111"],
        "answer": "B",
        "amount": 85000
    },
    {
        "question": "Which is the largest internal organ in the human body?",
        "options": ["Heart", "Brain", "Liver", "Lung"],
        "answer": "C",
        "amount": 86000
    },
    {
        "question": "Which company created the iPhone?",
        "options": ["Samsung", "Google", "Apple", "Microsoft"],
        "answer": "C",
        "amount": 87000
    },
    {
        "question": "Which Indian city is known as the Silicon Valley of India?",
        "options": ["Hyderabad", "Mumbai", "Bengaluru", "Pune"],
        "answer": "C",
        "amount": 88000
    },
    {
        "question": "Which function is used to get the type of an object in Python?",
        "options": ["kind()", "typeof()", "type()", "object()"],
        "answer": "C",
        "amount": 89000
    },
    {
        "question": "Which ocean lies between Africa and Australia?",
        "options": ["Atlantic", "Pacific", "Indian", "Arctic"],
        "answer": "C",
        "amount": 90000
    },
    {
        "question": "What is the chemical formula of water?",
        "options": ["CO2", "H2O", "O2", "NaCl"],
        "answer": "B",
        "amount": 91000
    },
    {
        "question": "Which keyword is used to create a class in Python?",
        "options": ["object", "class", "struct", "define"],
        "answer": "B",
        "amount": 92000
    },
    {
        "question": "Who was the first woman Prime Minister of India?",
        "options": ["Pratibha Patil", "Sarojini Naidu", "Indira Gandhi", "Sonia Gandhi"],
        "answer": "C",
        "amount": 93000
    },
    {
        "question": "Which protocol is commonly used to send emails?",
        "options": ["HTTP", "SMTP", "FTP", "SSH"],
        "answer": "B",
        "amount": 94000
    },
    {
        "question": "What is the main function of DNS?",
        "options": ["Encrypt files", "Translate domain names into IP addresses", "Store passwords", "Transfer emails"],
        "answer": "B",
        "amount": 95000
    },
    {
        "question": "Which Python method removes the last item from a list by default?",
        "options": ["remove()", "delete()", "pop()", "discard()"],
        "answer": "C",
        "amount": 96000
    },
    {
        "question": "Which Indian monument is located in Agra?",
        "options": ["Qutub Minar", "Gateway of India", "Taj Mahal", "Charminar"],
        "answer": "C",
        "amount": 97000
    },
    {
        "question": "Which scientist developed the theory of relativity?",
        "options": ["Isaac Newton", "Albert Einstein", "Marie Curie", "Niels Bohr"],
        "answer": "B",
        "amount": 98000
    },
    {
        "question": "What does API stand for?",
        "options": ["Application Programming Interface", "Advanced Program Integration", "Automated Programming Input", "Application Process Internet"],
        "answer": "A",
        "amount": 99000
    },
    {
        "question": "Which Python module is used to generate random numbers?",
        "options": ["os", "sys", "random", "math"],
        "answer": "C",
        "amount": 100000
    }
]

# print(Quiz["question"])

for i in range(1,10+1):
  print(f"You Won {amount}")
  choice=random.choice(questions)
  print(choice['question'])
  option_list="ABCD"

# Printing Options
# Why Enumerate ? Enumerate enumerate() is a Python built-in function that gives you two things while iterating:
# 1. Index – Position of an element.
# 2. Value – Actual element.
  for i, option in enumerate(choice["options"]):
      print(f"{option_list[i]} : {option}")

  anwser=input("Enter Option (A/B/C/D)").upper()
  if anwser not in  option_list:
     print("Invalid Answer")

  elif anwser==choice["answer"]:
     print("Correct Answer!")
     amount += choice["amount"]
     print(f"You won Rs. {amount}")
  else:
     print("Incorrect Answer")
     print("Game is over")
     print(f"The correct Answer is {choice['answer']}")
     break
  take_decision=input("Next-->Enter Any Key / Quit-->Q").upper()
  if take_decision=="Q":
     break
  
   



# Final result
print("\================================")
print(f"Mr/Mrs {name} congratulations !!! ")
print(f"Your final winning amount: Rs. {amount}")
print("================================")

print("\================================")
print(f"==========Check Details==========")
print(f"Name: {name}")
print(f"Email: {email}")
print(f"Phone: {phone}")
print(f"Bank Account: {bank_account}")



print("================================")
print("If there is any mistake in details contact with us")