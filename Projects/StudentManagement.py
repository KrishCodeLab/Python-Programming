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


def calculate_total(phy,che,math):
    total=phy+che+math
    return total   





  
