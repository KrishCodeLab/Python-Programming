# What is packing ? --> Packing means storing elements in one collection 
# Example: Tuple,list,set

# Packing
s=(100,234,5667,"Govardhane","Male")
print(s)

# What is Unpacking ? --> Unpacking means assigning tuple elements to separate variables.
# Unpacking Tuple Elements
student=("Krishna",20,"AIML")
name,age,course=student
print("Name of student : ",name)
print("Age of student : ",age)
print("Course of student : ",course)


# Swapping two numbers using unpacking
num=(101,1001)
a,b=num

print(a)
print(b)
print("====================")
a=10
b=1001

a,b=b,a
print(a)
print(b)

print("====================")


# Unpacking with * operator it converts all elements to list
numbers = (100, 20, 30, 40, 50, 60, 70)

first, *middle, last = numbers

print(first)
print(middle)
print(last)

print("====================")

# Unpacking with ignoring some values
student = ("Krish", 20, "AI", 85.5)

name, _, course, _ = student

print(name)
print(course)

# Unpacking nested tuple
print("===========================")
info=("Krihna",20,(90,95,99))
name,age,(math,english,aptitude)=info
print(name)
print(age)
print(math)
print(english)
print(aptitude)