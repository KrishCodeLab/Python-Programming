class Student:

 def __init__(self,name,rollno,phy,che,math,age,gender,college_name,department_name,semester_no,course_name,email):
    self.name=name
    self.rollno=rollno
    self.math=math
    self.phy=phy
    self.che=che
    self.age=age
    self.gender=gender
    self.college_name=college_name
    self.department_name=department_name
    self.semester_no=semester_no
    self.course_name=course_name
    self.email=email


 def calculate_total(self,phy,che,math):
    total=self.phy+self.che+self.math
    return total   



s=Student("Krishna",14,90,99,99,20,"male","Alard University x Niat","AIML",1,"AIML","kruhna@gmail.com")

print( s.calculate_total(90,99,99))


  
