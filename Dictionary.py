# Dictionary in python : A dictionary is a Python data structure used to store data in key-value pairs
# A dictionary in Python is used to store data in key-value pairs.
student = {
    "name": "Krish",
    "age": 20,
    "course": "AI"
}
print(student)
print(student["name"])

print(student["age"])

# Keys must be unique : You cannot have two separate entries with the same key. If you repeat a key, the last value is kept.
dict_a = {"age": 15, "age": 20}
print(dict_a)

# Keys must be immutable : Immutable means a value cannot be changed in place
name = "Teja"
# name[0] = "R" --> Raises Error

# Values can repeat : Values can be of any data type and can repeat.
dict_a={"age":20,"rollno":20}
print(dict_a)
print(dict_a["age"])
print(dict_a["rollno"])

# Dictionaries are mutable : Mutable means we can change the dictionary after creating it.


# Creating dictionary using dict()
student=dict()
print(student)

# Creating dictionary using {}
student={}
print(student)

# Accessing values of the dictionary
student = {
    "name": "Krish",
    "age": 20,
    "course": "AI"
}

print(student["name"])
print(student.get("name"))
print(student["age"])
print(student.get("age"))
print(student["course"])
print(student.get("course"))
# print(student["city"]) --> Raises keyError
print(student.get("city"))  # --> Returns none

# Membeship Operator
print("name" in student) #-->Returns true because name key exists in student dict
print("city" in student) #-->Returns false because city key does not exists in student dict
print("city" not in student) #-->Returns true because city is not exists in student dict