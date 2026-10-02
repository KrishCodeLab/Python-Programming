# Problem Statement :Create a BankAccount class with:

# Account holder name
# Account number
# Balance
# Deposit money
# Withdraw money
# Prevent negative balance
# Prevent invalid deposit/withdrawal amounts
# Use @property to control the balance
class BankAccount:

  def __init__(self,name,acc_number,balance):
    self.name=name
    self.acc_number=acc_number
    self.balance=balance

  @property
  def balance(self):
    return self._balance

  @balance.setter
  def balance(self,Value):
    if Value <= 0:
      print("Balance can't be negative")
    else:
      self._balance=Value

# Deposite money
  def deposite(self,Value):
    if Value > 0:
      self.balance +=Value
    else:
      print("You can't deposite negative value")   
# Withdraw money
  def withdraw(self,Value):
    if Value <= 0:
      print("Amount must be greater than 0 to withdraw")
    elif Value >self.balance:
      print("Insufficient Balance")
    else:
      self.balance -=Value

# Display Account information
  def information(self):
    print("Name of the account holder is : ",self.name)
    print("Account number of the account holder is : ",self.acc_number)
    print(f"Balance of {self.name} is {self.balance}")


b=BankAccount("Krishna",23412,50000)
b.information()
print(b.balance)
b.balance=80000
print(b.balance)
b.deposite(5000)
print(b.balance)
b.withdraw(2000)
print(b.balance)