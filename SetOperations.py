# isdisjoint() : Checks whether two sets have no common elements.
# Returns True if they have no common elements.Returns False if they share at least one element.
A={1,2,3}
B={4,5,6}
C={3,2,1}

print(A.isdisjoint(B)) #-->Returns True 
print(B.isdisjoint(C)) #-->Returns False
print(C.isdisjoint(A)) #-->Returns False


# issuperset() : Checks whether one set contains all the elements of another set
A = {1, 2, 3, 4, 5}
B = {2, 3}

print(A.issuperset(B)) #A contains all elements of the B so returns true
print(B.issuperset(A)) #B does not contains all elements of A so returns false


# issubset() : Checks whether all the elements of one set exist in another set.
A = {1, 2, 3, 4, 5}
B = {2, 3}

print(B.issubset(A))
print(A.issubset(B))

# A.issuperset(B) → A contains all elements of B.



# B.issubset(A) → All elements of B exist in A.

# 
