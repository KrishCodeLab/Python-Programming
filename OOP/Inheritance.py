# Inheritance : Inheritance in Object-Oriented Programming (OOP) is a core mechanism that allows a new class to acquire the properties and behaviors of an existing class

# • Parent Class (Superclass / Base Class): The original class whose attributes and methods are shared.
# • Child Class (Subclass / Derived Class): The new class that inherits from the parent class and can add its own unique features

class Animal: # Parent Class
  def eat(self):
    print("Animal is eating ")

# Dog is inherit from Animal class
class Dog(Animal):  # Child Class
  def bark(self):
    print("Dog is barking")

D=Dog()
# Dog class can access the eat function of the Animal because Dog class is iherited from Animal class
D.eat()
D.bark()