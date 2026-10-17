# Membership Operator : in and not in
# in ---> It is used to check the element is present in collection.
# not in ---> It is used to check the element is not present in collection.

student=("Krishna",20,9.6,"Nashik")
print("Krishna" in student) #Returns true if the Krishna is present in student else False
print("Nashik" in student) #Returns true if the Nashik is present in student else False
print("Rahul" not in student) #Returns true if the Rahul is not present in student because we used not in operator
print("Pune" in student) #Returns true if the pune is present in student else False
print(9.1  in student)