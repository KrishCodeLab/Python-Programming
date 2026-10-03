class Credit:
  def pay(self,amount):
    print(f"Paid ${amount} using credit card")

class UPI:
  def pay(self,amount):
    print(f"Paid ${amount} using UPI")

class Cash:
  def pay(self,amount):
    print(f"Paid ${amount} using cash")

def make_payment(payment_method, amount):
  payment_method.pay(amount)


make_payment(Credit(), 1000)
make_payment(UPI(), 500)
make_payment(Cash(), 200)