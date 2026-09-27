# Class and Instance Attribute

# class Attribute --> A class attribute is a variable declared inside a class but outside the methods. It is shared by all objects of that class

# Instance Attribute -->An instance attribute is a variable that belongs to a particular object. It is commonly created using self inside the constructor



# Class attribute = common data (college name, country, company name).
# Instance attribute = individual data (student name, roll number, marks).

class Student:
  college_name="MIT WPU"
  
  def __init__(self,name,marks):
    self.name=name
    self.marks=marks
    

s1=Student("Krishna",99,)
print(s1.name,s1.college_name,s1.marks)

s2=Student("Arjun",100)
print(s2.name,s2.college_name,s2.marks)

print(Student.college_name)

# Print MIT WPU
# print(s1.college)
# print(s2.college)
# print(Student.college)


s1.college_name="Alard University"
print(s1.college_name)
print(s2.college_name)
print(Student.college_name)