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

# os.path.getsize() : It Returns a size of file in bytes
path="data.txt"
size_of_file=os.path.getsize(path)
# Empty file returns 0 bytes
print(f"File size : {size_of_file} bytes")

# File that contains data returns number
path="Area.py"
size_of_file=os.path.getsize(path)
print(f"File size : {size_of_file} bytes")

# os.path.basename(path)

base_file_name=os.path.basename(r"C:\Users\Krushana\OneDrive\Desktop\Python Programming\data.txt")
print("Current Working File :",base_file_name)

# os.path.dirname() : Returns the parent directory 
path=r"C:\Users\Krushana\OneDrive\Desktop\Python Programming"
parent_folder=os.path.dirname(path)
print("Parent of Python Programmign folder is :",parent_folder)