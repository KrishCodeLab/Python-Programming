# What is difference between the class method,instance method,static method

# <--1--> class method :A class method is a method that works with the class-level data rather than a particular object's data.
# It uses cls as the first parameter.@classmethod decorator is use to implementation of classmethod
# It is use to access and modify the class level attributes and variables
# Use it when the information or operation is common to all objects of the class


# <--2--> instance method : An instance method is a method that works with the data of a particular object
# It uses self as the first parameter.There is no need of decorator 
# It is used to work with object's/instance's data
# Use it when the method needs information that is different for each object


# <--3--> static method : A static method is a method that does not depend on object data or class data.
# It does not uses any value as parameter to implement method.@staticmethod decorator is used to implementation of static method
# Used for a general-purpose operation that is logically related to the class.
# Use it when you need a function inside a class but the function doesn't need any information from the object or class.

class student:
  college="Alard University"

#  constructor 
  def __init__(self,name,marks):
    self.name=name
    self.marks=marks

#  instance method 
  def show_data(self):
    print(f"The name of the student is {self.name}")
    print(f"The marks of the student is {self.marks}")

# class method
  @classmethod
  def show_clg(cls):
    print(f"The college of the student is {cls.college}")

#static method
  @staticmethod
  def show_grade(marks):
    if marks >=90 and marks <=100:
      print("Grade A+")
    elif marks >=80 and marks <=89:
      print("Grade A")
    elif marks >=70 and marks <=79:
      print("Grade B")
    else:
      print("Grade C")

s=student("Sanskruti",93)
s.show_data()
s.show_clg()
s.show_grade(95)