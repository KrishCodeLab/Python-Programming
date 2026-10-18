class Person:
   def __init__(self,name,rollno):
      self.name=name
      self.rollno=rollno


class Student(Person):

 def __init__(self,name,rollno,phy,che,math,age,gender,college_name,department_name,semester_no,course_name,email):
    super().__init__(name,rollno)
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

 @staticmethod 
 def validate_mark(mark):
    if isinstance(mark,bool) or not isinstance(mark,(int,float)):
       raise ValueError("Marks must be a number !!! ")

    if mark < 0 or mark >100:
       raise ValueError("Marks must be between 0 to 100 ")

# access the internal mark using self.phy -->getter
 @property 
 def phy(self):
    return self.__phy

# setter 
 @phy.setter
 def phy(self,value):
    self.validate_mark(value)
    self.__phy=value

 
 @property
 def che(self):
    return self.__che

 @che.setter
 def che(self, value):
    self.validate_mark(value)
    self.__che = value


 @property
 def math(self):
    return self.__math

 @math.setter
 def math(self, value):
    self.validate_mark(value)
    self.__math = value

 

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


 @classmethod
 def from_percentage(
        cls, name, rollno,percentage, age, gender,
    college_name, department_name, semester_no,
    course_name, email
    ):
        # Assume all three subjects have equal marks
        return cls(
            name, rollno,
            percentage,percentage,percentage,
            age, gender, college_name, department_name,
            semester_no, course_name, email
        )

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

class StudentResultManager:
   def __init__(self):
      # Manage multiple Student objects
      self.students=[]
 


s=Student("Krishna",14,90,99,99,20,"male","Alard University x Niat","AIML",1,"AIML","kruhna@gmail.com")
print(s.calculate_total())
print( s.calculate_percentage())
s.calculate_grade()
# s.display_student_details(90,99,99)
print(s.phy)
# s.phy=-10 -->Raise ValueError

print("=============================================================================================================================")

s2=Student.from_percentage("Govardhane",14,94,20,"male","Alard University x Niat","CSE AI",1,"CSE","Govardhane@gmail.com")
print(s2.name)
s2.calculate_grade()
print(s2.calculate_percentage())
print(s2.phy)
print(s2.che)
print(s2.math)

print("=============================================================================================================================")

s3 = Student(
    "Rahul", 25, 85, 78, 92, 21, "Male",
    "Pune University", "CSE", 2,
    "Computer Science", "rahul@gmail.com"
)

print(s3.name)
print(s3.rollno)
print(s3.phy)
print(s3.che)
print(s3.math)
print(s3.college_name)
print(s3.calculate_percentage())
print(s3.calculate_total())
s3.calculate_grade()
