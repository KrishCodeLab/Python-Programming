# Create student class that takes name and marks of 3 subjects as arguments in constructor.Then create a method to print the average
class Student:

  def __init__(self,m1,m2,m3):
    self.m1=m1
    self.m2=m2
    self.m3=m3

  def CalculatAvg(self):
    avg=(self.m1+self.m2+self.m3)/3
    return avg


s1=Student(90,98,95)
print(f"{s1.CalculatAvg():.2f}")