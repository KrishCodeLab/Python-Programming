class Student:

 def __init__(self,name,rollno,phy,che,math,age,gender,college_name,department_name,semester_no,course_name,email):
    self.name=name
    self.rollno=rollno
    self.__math=math
    self.__phy=phy
    self.__che=che
    self.age=age
    self.gender=gender
    self.college_name=college_name
    self.department_name=department_name
    self.semester_no=semester_no
    self.course_name=course_name
    self.email=email

 @staticmethod 
 def validate_mark(mark):
    if isinstance(mark,bool) or not isinstance(mark,(int,float)):
       raise ValueError("Marks must be a number !!! ")

    if mark < 0 or mark >100:
       raise ValueError("Marks must be between 0 to 100 ")
       
 
 

 def calculate_total(self):
    self.total=self.phy+self.che+self.math
    return self.total   

 def calculate_percentage(self):
   self.total=self.calculate_total()
   self.percentage=self.total/3
   return self.percentage
 def get_result(self):
    if self.phy>=35 and self.che >=35 and self.math>=35:
       return True
    else:
       return False


    
 def calculate_grade(self):
   if self.get_result() ==True:
         
         self.percentage=self.calculate_percentage()
         if self.percentage >100 or self.percentage <1:
            print("Invalid Percentage!!!")
         elif self.percentage >=90:
            print("Grade A+")
         elif self.percentage>=80:
            print("Grade A")
         elif self.percentage>=70:
            print("Grade B")
         elif self.percentage >=60:
            print("Grade C")
         else:
            print("Grade D")
   else:
      print("Student must have atleast 35 marks in each subject")

  # get result method
 def display_student_details(self):
       # Display the name, roll number, subject marks, total, percentage, grade, and result
      print("=============================================================================================================================")
      print("Student Name : ",self.name)
      print("College Name : ",self.college_name)
      print("Roll No : ",self.rollno)
      self.percentage=self.calculate_percentage()
      self.total=self.calculate_total()
      print("Total marks of the student out of 300 is : ",self.total)
      print("The Percenatage of the student : ",self.percentage)
      print("=============================================================================================================================")

  # Goal: Return PASS if every subject has at least 35 marks; otherwise, return FAIL

  
 


s=Student("Krishna",14,90,99,99,20,"male","Alard University x Niat","AIML",1,"AIML","kruhna@gmail.com")
print(s.calculate_total())
print( s.calculate_percentage())
s.calculate_grade()
# s.display_student_details(90,99,99)

  
