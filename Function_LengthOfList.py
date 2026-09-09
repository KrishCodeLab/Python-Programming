# Print the length of list,string,tuple

def length_of_list(list):
  return len(list);

def length_of_string(str):
  return len(str)

def length_of_tuple(tup):
  return len(tup)

list=[1,2,3,4,5,6,7,8,9,10]
print(length_of_list(list));

str=input("Enter string ")
print(length_of_string(str))

tup=(2,4,6,8,10)
print(length_of_tuple(tup))
