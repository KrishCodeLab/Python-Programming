# a property is a way to control how an object's attribute is read, changed, or deleted, while still letting you access it like a normal attribute.
# It allows us to control:
# Reading a value
# Changing a value
# Validating a value
class Student:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self,value):
        

        # add Validation to check data
        if value <= 0:
            print("Age can't be negative value ")
        else:
            self._age=value
            print("Age is updated successfully")

s=Student(20)
# We can access age method like attribute of the class
print(s.age)
# We can't access method like method because we set it as property
# print(s.age()) -->Error
s.age=34
print(s.age)
s.age=-3
s.age
