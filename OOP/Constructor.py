# Constructor : It is special member function in python which will automatically called when the instance of the class is created
# __init__(self)

# There are two main types of constructor in python :
# 1-->Default constructor : A constuctor without the parameter and the constructor with default paramter is call default constructor like __init__(self)

# 2-->Parameterized constructor :A constuctor with a parameter is call parameterized constructor like __init__(self,name,rollno)

# Create a simple class whether simply used concepth of constructor like default and parameterized 

class student:
  name=""
  roll=0
  marks=0

  
  print("Welcome to the student dashboard")

  def __init__(self,name,roll,marks):
    self.name=name
    self.roll=roll
    self.marks=marks

  def display(self):
    print("Student Name  : ",self.name)
    print("Student Roll  : ",self.roll)
    print("Student Marks  : ",self.marks)



s1=student("krishna",21,98)
print(s1.name,s1.roll,s1.marks)
s1.display()