# OS.isfile() : Checks whether is it file or not
import os

path="data.txt"

if os.path.isfile(path):
  print("It is file ")
else:
  print("Is is not file ")

# os.isdir() : Check whether is it folder or not
path="Projects"
if os.path.isdir(path):
  print("It is folder")
else:
  print("It is not folder")

# print(os.listdir())

# 

