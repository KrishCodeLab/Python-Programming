# OOP Concept: Class and Object

# Creating a class
class Student:

    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


# Creating objects of the Student class
student1 = Student("Krushna", 20)
student2 = Student("Rahul", 21)

# Calling the method using objects
student1.display()
student2.display()