# What is Polymorphism ? 
# It means One name , many functions , Poly -> Many and Morph -> Forms 
class Dog:
    def sound(self):
        print("Woof")

class Cat:
    def sound(self):
        print("Meow")

Dog=Dog()
Dog.sound()
Cat=Cat()
Cat.sound()

# The action is same sound but the behaviour is different