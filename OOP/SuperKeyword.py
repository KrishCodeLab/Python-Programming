# Super Keyword : he super() function is used inside a child class to access the parent class's methods or constructor
class Student:
  def __init__(self,name,id):
    self.name=name
    self.id=id
    print(self.name)
    print(self.id)

class Exam(Student):
  def __init__(self,name,id,course):
    print("Data is Shown below")
    super().__init__(name,id)
    self.course=course
    print(self.course)

e=Exam("Ram",345,"Computer")
print("------------Methods returns output here after that we are accessing particular attribute-------------")
print(e.name)
print(e.id)
print(e.course)