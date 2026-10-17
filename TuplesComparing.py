# Tuples Comparing : Python compares tuples element by element, starting from the first element
f=(1,2,3,4,5)
s=(1,2,3,4,5)
print(f==s)

# Python compares two tuples
print((10, 20) == (10, 20))

# Compares first element first if the first elements are same then second element then returns the true or false
print((10, 20) < (10, 30))

# Compares first element if it is not same return true or false immediatly
print((5, 100) < (6, 1)) # This is called lexicographical comparison.