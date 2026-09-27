# It is a programming approach in which we organize our code using classes and objects instead of writing everything separately.

# In simple words, OOP allows us to combine data (variables) and functions (methods) into one unit.

# creating class
class student:
  name="Krushna Govardhane"

  def __init__(self,fullname):
    self.name=fullname


# creating object of class
# s1=student()
# print(s1.name) -->krushna govardhane
# s2=student()
# print(s2.name) -->krushna govardhane
s3=student("KrishnaGovardhane")
print(s3.name) #-->KrishnaGovardhane