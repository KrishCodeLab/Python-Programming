# Encapsulation is the process of combining data (variables) and methods (functions) into a single unit called a class and controlling access to the data.
# Real-life example

# Think about an ATM machine.

# You can check your balance and withdraw money.

# You cannot directly access or modify the bank's internal database.

# The ATM provides controlled access through buttons and options.


class BankAccount:
  previous_Balance=0
  def __init__(self,balance,name):
    self.balance=balance
    self.name=name

  def Diposit(self,Amount):
    self.previous_Balance=self.balance
    self.balance +=Amount
    print(f"Deposited: {Amount}")

  def CheckBalance(self):
    print(f"The Bank Balance of {self.name} is {self.balance}")
    print(f"The Previous Balance of {self.name} is {self.previous_Balance}")

  def Credit(self,Credit_Amount):
    self.balance=self.balance-Credit_Amount
    print(f"The {Credit_Amount} is credtied from {self.name}'s account .Now your current balance is : {self.balance}")
    print(f"Withdrawn: {Credit_Amount}")
    print(f"Current Balance: {self.balance}")

b=BankAccount(34500,"Krishna Govardhane")
b.Diposit(4000)
b.CheckBalance()
b.Credit(300)



