# Inheritance with private attribute and methods
# Create a parent class BankAccount with:

# Private attribute __balance
# Method show_balance() to display the balance
# Method deposit(amount) to add money

# Create a child class SavingsAccount that inherits from BankAccount.

# The child class should have:

# Method add_interest() that adds ₹500 to the account
# Use the parent's methods to display and modify the balance.

class BankAccount: #Parent class
  def __init__(self,balance):
    self.__balance=balance
    

  def show_balance(self):
    print(self.__balance)

  def deposite(self,amount):
     self.__balance += amount
     

class TaxCalculator(BankAccount): #Child class
    
    def add_intrest(self):
      self.deposite(500)

account=TaxCalculator(20000)
print("Account Balance : ",account.show_balance())
account.deposite(5000)
print("Account After Deposite",account.show_balance())
account.add_intrest()
print("Account After intrest added",account.show_balance())

      
