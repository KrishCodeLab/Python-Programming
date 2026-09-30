# Private Attributes and Methods : A private attribute is an attribute that we don't want to access directly from outside the class
# In Python, we usually make it private by using two underscores __ before its name.

class Student:

  def __init__(self,name,marks,pin):
    self.name=name
    self.__marks=marks  # Marks attribute is private
    self.pin=pin 


#  Accessing private attribute outside the class using class method
  def get_marks(self):
    print(self.__marks)

# Private Methods : A private method is a method that is intended to be used inside the class, rather than directly from outside.
  def __get_pin(self):
    print(self.pin)

  def printPin(self):
    self.__get_pin()

s=Student("Krishna",99,2029)
print(s.name)
# print(s.marks) --> Error Because marks is private attribute
s.get_marks()
# s.__get_pin() --> Private Method 
s.printPin()