# Dictionary Operations : Adding a new item , Modifying an existing item , Deleting an item using del 
student={
  "name":"krishna",
  "age":20,
  "course":"CSE AI"

}

# Adding a new item
student["city"]="Pune"
print(student)

student["Role"]="AI Engineer"
print(student)

# Modifying an existing item
student["Role"]="AI Scientist"
print(student)

# Deleting an item using del
del student["age"]
print(student)