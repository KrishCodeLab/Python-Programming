# Dictionary Methods : 
student={
  "name":"krishna",
  "age":20,
  "course":"CSE AI"
}

# keys() : Returns all keys.
print(student.keys())

# values() Returns all values.
print(student.values())

# dict.items() : returns dictionary items(key-value) pairs
print(student.items())

# Iterate over Dictionary Views
for key in student.keys():
  print(key)

# List of the keys 
dict_list=list(student.keys())
print(dict_list)

# Iterate over Dictionart views 
for value in student.values():
  print(value)

# List of the values
dict_values=list(student.values())
print(dict_values)

# Tuple of keys
dict_tuple_keys=tuple(student.keys())
print(dict_tuple_keys)


# Iterate key value both usign items() methods
for key,value in student.items():
  print(key,value)
  pair="{} {}".format(key,value)
  print(pair)

  # keys() , values() & items() are called Dictionary Views as they provide a dynamic view on the dictionary’s items.
  views=student.keys()
  print(views)

  views=student.values()
  print(views)

  # Sequence to Dictionary
  list_stu=[
    ("name","David"),
    ("age",20),
    ("course","AIML")
  ]

  list_to_dict=dict(list_stu)
  print(list_to_dict)

  for key,value in list_to_dict.items():
    print(key , value)