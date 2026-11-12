# Exception handling in File I/O
# with open("unknown.txt", "r") as file:
#     # Error --> FileNotFound
#     # print(file.read())


try:
    with open("unknown.txt","r") as file:
      print(file.read())

except FileNotFoundError:
    print("File does not exist")

except PermissionError:
    print("You don't have permission to access file content")

except OSError as e:
    print("Fiel Operation Failed ",e)

try:
    with open("unknown.txt","x") as file:
        file.write("New Student")
except FileExistsError:
    print("File Already Exist !!! ")
    