class Vehile:
  def __init__(self,name,marks):
    self.name=name
    self.marks=marks

  def welcome(self):
    print("Car Name :",self.name)

  def get_marks(self):
    return self.marks 


v1=Vehile("Krishna",99)
# print(v1.welcome())
v1.welcome()

print(v1.get_marks())