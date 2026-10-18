# Set operations : Sets become especially powerful when you compare two collections. Python supports the same operations used in mathematics.
student_a = {"Python", "Java", "SQL", "HTML"}
student_b={"Python","Javascript","SQL","CSS"}

# Union : Combines both sets and returns new set as result.
# Result contains every unique element found in either set.
print(student_a.union(student_b))
print(student_a | student_b)

numbers = {1, 2, 3}

result = numbers.union([3, 4, 5])

print(result)



result = numbers | {3, 4, 5}
print(result)



# Intersection (&) — find common elements
print(student_a & student_b)
print(student_a.intersection(student_b))

# Returns the common number 
# intersections with list
result=numbers.intersection([3,4,5])
print(result)


# intersections with tuple
result=numbers.intersection((1,2,3))
print(result)

# Difference (-) — find elements in A but not B
# What elements are in one set but not the other ?
 
# difference() method and - operator returns the elements that exists in A but not in B
print(student_a.difference(student_b))
print(student_a-student_b)
# Returns the elements that exists in B but not in A
print(student_b.difference(student_a))


# The symmetric_difference() method or ^ operator returns elements that exist in A or B, but not in both.
# Returns unique elements of the both sets.
A = {10, 20, 30, 40}
B = {30, 40, 50, 60}

print(A ^ B)
print(A.symmetric_difference(B))

print(student_a ^ student_b)
print(student_a.symmetric_difference(student_b))

A = {10, 20, 30, 40}
B = {30, 40, 50, 60}

# Returns all unique elements from A and B
print(A.union(B))

# Returns elements common to both A and B
print(A.intersection(B))

# Returns elements present in A but not in B
print(A.difference(B))

# Returns elements unique to either A or B, excluding common elements
print(A.symmetric_difference(B))