# Tuple contains list inside tuple
info=(10,20,30,[100,200,300])
print(info)

for i in info:
  print(i)
print("================================")
# Tuples are immutable in python but list is mutable we can modify list that exists in tuple
info[3].append(400)
for i in info:
  print(i)