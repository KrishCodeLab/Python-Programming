# Single Level Inheritance : One child class inherits properties and methods from one parent class.
class car:
  def __init__(self,name):
    self.name=name

  def start(self):
    print("Car is started...")

class Variant(car):
  def color(self,color):
    self.color=color
    print(f"{self.color} car")

  def stop(self):
    print("Car is stoped")

v=Variant("Harrier")
v.start()
v.color("Black")
v.stop()