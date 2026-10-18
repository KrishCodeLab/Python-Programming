# What is set : Set is mutable so we can add or remove the elements.Set is data structure in python that stores unique elements in unordered manner.
numbers={10,20,30,40,10,20,30,40}
# Python automatically removes the duplicate values from set.
print(numbers)

# Implementing set using {} 
fruits={"apple","mango","banana","pineapple"}
print(type(fruits))

# Implementing set using set()
# num=set(1,2,3,4,5) #--> Returns the error because set expecting only one argument 
num=set([1,2,3,4,1,2,5,1]) #--> Returns the set because we passed multiple values as one argument using list
print(type(num))
print(num)


# You can convert a list, tuple, string, or other iterable into a set.
string=set("Kruhna Govardhane")
print(string)


student=["Bob",20,7.7]
student_Set=set(student)
print(student_Set)

student_tuple=(1,2,3,4,5)
student_Set=set(student_tuple)
print(student_Set)


# Implmenting empty set
empty_set={} #--> Created
print(type(empty_set))

empty_set=set()
print(type(empty_set))