# Write a function that print the information of the 4 students


def student_information(name,email,college,department,id,phone,percentage):
        print("--------------------------------------------Student Data-------------------------------------------")
        print()
        print()
        print("Student Name:", name)
        print("Email:", email)
        print("College:", college)
        print("Department:", department)
        print("ID:", id)
        print("Phone:", phone)
        print("Percentage:", percentage)
   



student_name=input("Enter student name : ")
student_department=input("Enter student department : ")
student_id=int(input("Enter student id : "))
student_percentage=float(input("Enter student percentage : "))
student_collegeName=input("Enter college name")
student_email=input("Enter student email id : ")
student_phoneNo=int(input("Enter student phone No : "))


student_information(student_name,student_email,student_collegeName,student_department,student_id,student_phoneNo,student_percentage)