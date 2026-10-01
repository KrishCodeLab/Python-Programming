# Multi level Inheritance : Multilevel inheritance means inheritance happens in multiple levels.
# Grandparent class
class Grandfather:

    def house(self):
        print("Grandfather has a house")


# Parent class
class Father(Grandfather):

    def car(self):
        print("Father has a car")


# Child class
class Son(Father):

    def bike(self):
        print("Son has a bike")


# Create object of Son
s = Son()

s.house()
s.car()
s.bike()