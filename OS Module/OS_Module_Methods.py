import os

# os.getcwd(): Get current working directory 

current_working_dir=os.getcwd()
print(current_working_dir)


# os.listdir() : List files and folders
folder_list=os.listdir()
print(folder_list)

# os.mkdir() : Create nested directory and Returns nothing 
# imp : Once You Create Directory you can't create duplicate Directory with same name
# os.mkdir("Java Remaning Question")
# print(folder_list)

# os.path.exists() : Checks wither given folder or file exists in os.
if os.path.exists("Java Remaning Question"):
  print("File Exits")
else:
  print("File does not exits")


# Specified Path : The r tells Python to treat backslashes literally.
files = os.listdir(r"C:\Users\Krushana\OneDrive\Desktop")
print(files)


# os.mkdirs() : Creates multiple directories including parent directory
os.makedirs("Krushna/Krushna_Govardhane/Krushna_Govardhane_Btech",exist_ok=True)
folder_list=os.listdir()
print(folder_list)

#    os.mkdir()             	   os.makedirs()
# Creates one directory	    Creates nested directories
# Parent must exist	Can     Create missing parents


# os.rmdir() : Removes empty directory
os.rmdir("Java Remaning Question")
print(os.listdir())

# os.removedirs() : Remove nested directory with parent directory . 
os.makedirs("Python/Projects/OS_Module")
print(os.listdir())
os.removedirs("Python/Projects/OS_Module")
print(os.listdir())
