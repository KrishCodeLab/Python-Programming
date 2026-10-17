# Built in function
numbers=(1,7,38,8,2,4,9,0,21)
print("Length of tuple is : ",len(numbers))
print("Maxmimum of tuple is : ",max(numbers))
print("Minimum of tuple is : ",min(numbers))
print("Maxmimum of tuple is : ",max(numbers))
print(sorted(numbers)) # Returns sorted list not tuple

# If we want sorted tuple
print(tuple(sorted(numbers)))
