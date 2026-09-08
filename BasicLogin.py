# Question : Login System

# Create a simple login system.

# Ask the user for:

# Username:
# Password:
# email:

# Rules:
 
# First check whether the username is correct.
# If username is correct, check the pasl"
# If username is correct but password issword.
# If both are correct → "Login successfu wrong → "Wrong password"
# If username is wrong → "Wrong username"

username=input("Enter username : ")
password=input("Enter password : ")

if username=="Krishna@gmail.com":
  if password=="Krish12345":
    email=input("Enter email to on two step authentication ")

    print("You have a chance to change your password if you want to change it then enter yes neither no ")
    req=input("Enter req ")
    if req=="yes" or req=="Yes":
      password=input("Enter your new password")
      print("Your password is successfully changed ")
    elif req=="no" or req=="No":
      print("Your acccount password is not modified...")
    else:
      print("Wrong Request for password change try later")
    
    
    print("Login Successfully...")
  else:
    print("Password is incorrect... Please try again later")

else:
  print("Invalid Username...The user does not exits")