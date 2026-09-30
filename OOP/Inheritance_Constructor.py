# Inheritance with constructor : 
# When a child class does not have its own __init__(), it can use the parent class constructor.
# When a child class has its own __init__(), the parent constructor is not automatically called.


class Student: # Parent class
  def __init__(self,name):
    self.name=name

  def study(self):
    print(f"{self.name} is studying")

class EngineeringStudent(Student): # Child Class
  def coding(self):
    print(f"{self.name} is coding") # Access name from parent class constructor 


s1=EngineeringStudent("Krish")
s1.study()
s1.coding()