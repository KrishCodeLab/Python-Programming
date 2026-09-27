# Self Keyword in python

class student:
  name=""
  rollno=0
# init : It is uded to give an object its iniitial infromation when the object is created
  def __init__(self,fullname,rollno):
    self.name=fullname
    self.rollno=rollno
    # The Self parameter is reference to the current instance of the class and is used to access variables that belong to the class
    
    print(self)#Address of the object 

s1=student("Sara",23)
print(s1.name)
print(s1.rollno)

s2=student("Sam",24)
print(s2.name)
print(s2.rollno)