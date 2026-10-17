numbers=(10,57,35,67,43,75,76)
print(numbers)
print(type(numbers))

# Tuples are immutable 
print(numbers[1])
# numbers[1]=10 We can't modify 

# If we want to modify tuple , tuple should be converted to list
numbers_list=list(numbers)
print(numbers_list)

# Now we can modify the list
numbers_list[1]=100
numbers_list[3]=121

print(numbers_list)

# Now list should be converted to tuple again 
numbers=tuple(numbers_list)
print("Modified tuple : ")
print(numbers)