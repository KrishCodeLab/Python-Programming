# Static Method : Methods that don't use the self parameter work at class level

# What is Decorator : Decorator allows us to wrap another fucntion in order to extend the behaviour of the wrapped function,without
# permently modifying it

class Student:
  @staticmethod #Decorator
  def college():
    print("I am from Alard University x NIAT")

  @staticmethod #Decorator
  def DisplaySubject():
    print("Math")
    print("Aptitude")
    print("HTML")
    print("Python")


s=Student()
s.college()
s.DisplaySubject()


