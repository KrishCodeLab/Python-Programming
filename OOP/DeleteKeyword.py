# Delete Keyword : It is used to delete object properties of object itself.
# Object Allocates memory , to dellocate that memory del keyword is used

class DeleteKeyword:

  name="Rashmika"
  list_1=[1,2,3,4,5,6]

  del list_1[2] #Deletes the 3 from list

  def __init__(self,name,id,college):
    self.name=name
    self.id=id
    self.college=college

  def Deleteid(self):
    del self.id

  del name  
  # print(name)  # Error

d=DeleteKeyword("Smruti",1001,"MIT WPU")
print(d.name)
print(d.id)
print(d.college)
d.Deleteid()
# print(d.id) --> Return Error after deletion
del d
# print(d.name) --> Return Error because d object is deleted from memory

  