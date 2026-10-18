# Set Manipulation : Adding and Removing Elements from set
skills = {"Python", "Java"}

# Adding an element that already exists does not create a duplicate.
skills.add("SQL")
print(skills)

# Add multiple elements using update method
# update() accepts an iterable and adds its elements individually.
skills.update(["SQL", "HTML", "CSS"]) #-->Python Rejects Dulicate values
print(skills)


# remove() --> It removes the specified element from set
numbers={1,2,3,4,5}
numbers.remove(2) #--> Removes the 2 from set
print(numbers)

numbers.remove(1) #--> Removes the 1 from set
print(numbers)

# Python raises keyError if the element does not exist in set
# numbers.remove(10) #--> Error

# discard() --> It also removes specified element safely without raiseing any error
numbers.discard(100)
print(numbers)

# pop() — Remove and return an arbitrary element
# Unlike remove() and discard(), pop() does not accept an element as an argument. It removes and returns an arbitrary element from the set.

student_info={"Krish","Jay Shree Krishna",20,9.9}
removed=student_info.pop()
print("Removed ",removed)
print("Remaining ",student_info)


# clear : Removes all elements from set
student_info.clear() #--> Returns empty set
print(student_info) 